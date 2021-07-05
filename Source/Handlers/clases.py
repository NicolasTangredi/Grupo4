from time import sleep
import pandas
from ..Handlers import PuntosAciertos
from ..Handlers import usuario
from ..Handlers import timer as t

class Jugada():
    ''' es el controlador de la jugada, lleva la cuenta de los 
        elementos clickeados y si son iguales.
        para agregar un elemento se hace obj.update( boton, dato del boton )
        para reiniciar los elementos se hace obj.limpiar( tipo de dato )
    '''

    def __init__(self, config, maxAc):
        niveles = ['facil', 'medio', 'dificil']

        # configuracion
        self._tipo = config["tipo_elemento"]
        self._max = config["cant_coincidencias"]
        self._dificultad = niveles[(config['tiempo'] - 30) % 30]
        
        # contadores
        self._aciertos = 0
        self._maxAc = maxAc
        self._elems = []
        self._botones = []
        self._pointt = 0
        
        self._numJug = 0
        try:
            numJugAct = self._abrir_registro().tail(1)["partida"].values[0]
            self._numJug = (numJugAct + 1)
        except KeyError:  
            pass

        self._registrar_jugada('inicio_partida', self._numJug)

    def update(self, boton, dato,tiempo):
        ''' recibe el boton que fue clickeado y sus datos para
            chequear que sean iguales y si tiene todas las coincidencias
        '''

        self._elems.append(dato)
        self._botones.append(boton)

        # si el primer elemento aparece en todo el arreglo
        esIgual = self._elems.count(self._elems[0]) == len(self._elems)
        point = self._pointt
        # si se equivoco o llego al max de coincidencias
        if( not esIgual):
            #calcula la puntuacion del jugador si la jugada fue buena y actualiza la puntuacion en su perfil
            self._pointt = PuntosAciertos.calcular_puntos(
                False,
                point,
                self._dificultad
            )
            
            self._mala(dato,tiempo)
        elif ( len(self._elems) == self._max):
            #calcula la puntuacion del jugador si la jugada fue buena y actualiza la puntuacion en su perfil
            point = PuntosAciertos.calcular_puntos(True, point, self._dificultad)
            self._pointt = point
            print(point)
            return self._buena(dato,tiempo)

    def finalizar(self):
        user = usuario.usuario_conectado_profile()
        PuntosAciertos.pro_o_manco(True, user["nombre"])
        
        #falta una funcion para retornar el tiempo sobrante despues de la partida
        
        def tiempo_sobrante(user):
            return 0

        puntuacion_total = PuntosAciertos.fin_juego(
            self._pointt,
            self._aciertos,
            tiempo_sobrante(user),
            user
        )
        #si la puntuacion fue mayor que su puntaje maximo entonces la actualiza
        max = PuntosAciertos.points_max(user,self._dificultad)
        
        PuntosAciertos.sos_pro(
            max,
            puntuacion_total,
            user["nombre"],
            self._dificultad
        )
        #pone en 0 la casilla in game del usuario

    # --------------------- FUNCIONES PRIVADAS NO LLAMAR ---------------------

    def _mala(self, dato,tiempo):
        ''' pone los casilleros en blanco y reinicia los elementos y botones guardados
        '''
        sleep(0.5)
        for boton in self._botones:
            if(self._tipo == 'imagenes'):
                boton.update(image_data="", image_size=(100,102), disabled=False)
            else:
                boton.update("", disabled=False)
        
        self._limpiar()
        palabra = 'imagen' if (self._tipo == 'imagenes') else dato
        self._registrar_jugada('intento', self._numJug, 'error', palabra,tiempo)

    def _buena(self, dato,tiempo):
        """ Logica de un turno con todas las coincidencias 
            cuena los aciertos y da final a la partida
        """
        self._aciertos += 1
        self._limpiar()

        # termino la jugada y gano
        if( self._aciertos == self._maxAc):
            self.finalizar()
            return True
        else:
            palabra = 'imagen' if (self._tipo == 'imagenes') else dato
            self._registrar_jugada('intento', self._numJug, 'ok', palabra,tiempo)

    def _limpiar(self):
        """ limpia las listas de tarjetas clickeadas """
        self._elems.clear()
        self._botones.clear()

    def _abrir_registro(self):

        """ abre el archivo que registra las jugadas y turnos """
        try:
            with open('./data/stats.csv', "r+") as file:
                return pandas.read_csv(file)
        except:
            return pandas.DataFrame()

    def _registrar_jugada(self, evento, numJug, estado=None, palabra=None, tiempo = 0):
        user = usuario.usuario_conectado_profile()
        dataframe = self._abrir_registro()
        
        config = user['configuracion']
        num, num2 = config['cant_casillas'].split('x')
        elem = int(num) * int(num2) // config['cant_coincidencias']
        
        niveles = ['facil', 'medio', 'dificil']
        nivel = niveles[(config['tiempo'] - 30) % 30]
        
        data = {
            'tiempo': tiempo, 
            'partida': numJug, 
            'cant_elementos': elem, 
            'evento': evento, 
            'nombre': user['nombre'], 
            'genero': user['genero'], 
            'edad': user['edad'], 
            'estado': estado, 
            'palabra': palabra, 
            'nivel': nivel
        }

        dataframe = dataframe.append(data, ignore_index=True)
        dataframe.to_csv('./data/stats.csv', index=False)


        