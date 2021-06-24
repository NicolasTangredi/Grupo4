from time import sleep
import pandas
from ..Handlers import PuntosAciertos
from ..Handlers import usuario

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
        
        file = self._abrir_registro()
        self._numJug = len(file)

        self._registrar_jugada('inicio_partida', self._numJug)

    def update(self, boton, dato):
        ''' recibe el boton que fue clickeado y sus datos para
            chequear que sean iguales y si tiene todas las coincidencias
        '''

        self._elems.append(dato)
        self._botones.append(boton)

        # si el primer elemento aparece en todo el arreglo
        esIgual = self._elems.count(self._elems[0]) == len(self._elems)
        point = 0
        # si se equivoco o llego al max de coincidencias
        if( not esIgual):
            #calcula la puntuacion del jugador si la jugada fue buena y actualiza la puntuacion en su perfil
            point = PuntosAciertos.calcular_puntos(
                False,
                point,
                self._dificultad
            )
            
            PuntosAciertos.update_accumulated_points(usuario.usuario_conectado_profile(),point)
            self._mala(dato)
        elif ( len(self._elems) == self._max):
            #calcula la puntuacion del jugador si la jugada fue buena y actualiza la puntuacion en su perfil
            point = PuntosAciertos.calcular_puntos(True, point, self._dificultad)
            PuntosAciertos.update_accumulated_points(usuario.usuario_conectado_profile(), point)
            return self._buena(dato)

    def finalizar(self):
        user = usuario.usuario_conectado_profile()
        PuntosAciertos.pro_o_manco(True, user["nombre"])
        
        #falta una funcion para retornar el tiempo sobrante despues de la partida
        
        def tiempo_sobrante(user):
            return 10

        puntuacion_total = PuntosAciertos.fin_juego(
            PuntosAciertos.puntuacion_acumulada(),
            self._aciertos,
            tiempo_sobrante(user),
            user
        )
        #si la puntuacion fue mayor que su puntaje maximo entonces la actualiza
        PuntosAciertos.sos_pro(
            user["estadisticas"]["puntaje_maximo"],
            puntuacion_total,user["nombre"]
        )
        #pone en 0 la casilla in game del usuario
        PuntosAciertos.clear_accumulated_points(user)

    # --------------------- FUNCIONES PRIVADAS NO LLAMAR ---------------------

    def _mala(self, dato):
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
        self._registrar_jugada('intento', self._numJug, 'error', palabra)

    def _buena(self, dato):
        """ Logica de un turno con todas las coincidencias 
            cuena los aciertos y da final a la partida
        """
        self._aciertos += 1
        self._limpiar()

        # termino la jugada y gano
        if( self._aciertos == self._maxAc):
            self._registrar_jugada('fin', self._numJug)
            self.finalizar()
            return True
        else:
            palabra = 'imagen' if (self._tipo == 'imagenes') else dato
            self._registrar_jugada('intento', self._numJug, 'ok', palabra)

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

    def _registrar_jugada(self, evento, numJug, estado=None, palabra=None):
        user = usuario.usuario_conectado_profile()
        dataframe = self._abrir_registro()
        
        config = user['configuracion']
        num, num2 = config['cant_casillas'].split('x')
        elem = int(num) * int(num2) // config['cant_coincidencias']
        
        niveles = ['facil', 'medio', 'dificil']
        nivel = niveles[(config['tiempo'] - 30) % 30]

        data = {
            'tiempo': config['tiempo'], 
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
        dataframe.to_csv('./data/registro_jugadas.csv', index=False)


        