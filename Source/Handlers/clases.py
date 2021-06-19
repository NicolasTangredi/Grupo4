from time import sleep
from ..Handlers import PuntosAciertos
from ..Handlers import usuario

class Jugada():
    ''' es el controlador de la jugada, lleva la cuenta de los 
        elementos clickeados y si son iguales.
        para agregar un elemento se hace obj.update( boton, dato del boton )
        para reiniciar los elementos se hace obj.limpiar( tipo de dato )
    '''

    def __init__(self, tipo, coincidencias, maxAc):
        self.tipo = tipo
        self.aciertos = 0
        self.maxAc = maxAc
        self.elems = []
        self.botones = []
        self.max = coincidencias

    def update(self, boton, dato):
        ''' recibe el boton que fue clickeado y sus datos para
            chequear que sean iguales y si tiene todas las coincidencias
        '''

        self.elems.append(dato)
        self.botones.append(boton)

        # si el primer elemento aparece en todo el arreglo
        esIgual = self.elems.count(self.elems[0]) == len(self.elems)

        # si se equivoco o llego al max de coincidencias
        point = 0
        if( not esIgual):
            #calcula la puntuacion del jugador si la jugada fue buena y actualiza la puntuacion en su perfil
            point = PuntosAciertos.calcular_puntos(False,point,PuntosAciertos.que_dificultad_papa(PuntosAciertos.get_time()))
            PuntosAciertos.update_accumulated_points(PuntosAciertos.usuario_conectado_profile(),point)
            self.mala()
        elif ( len(self.elems) == self.max):
            #calcula la puntuacion del jugador si la jugada fue buena y actualiza la puntuacion en su perfil
            point = PuntosAciertos.calcular_puntos(True,point,usuario.que_dificultad_papa(usuario.get_time()))
            PuntosAciertos.update_accumulated_points(usuario.usuario_conectado_profile(),point)
            self.buena()

    def mala(self):
        ''' pone los casilleros en blanco y reinicia los elementos y botones guardados
        '''
        
        # espera un rato y luego pone los botones en blanco
        sleep(0.5)
        for boton in self.botones:
            if(self.tipo == 'imagenes'):
                boton.Update(image_data="", image_size=(100,102), disabled=False)
            else:
                boton.Update("", disabled=False)

        self.elems.clear()
        self.botones.clear()

    def buena(self):
        self.aciertos += 1
        self.botones.clear()
        self.elems.clear()

        # termino la jugada y gano
        if( self.aciertos == self.maxAc):
            user = usuario.usuario_conectado_profile()
                                            #falta una funcion para retornar el tiempo sobrante despues de la partida
            puntuacion_total = PuntosAciertos.fin_juego(PuntosAciertos.puntuacion_acumulada(),PuntosAciertos.aciertos(),tiempo_sobrante(user),user)
            #si la puntuacion fue mayor que su puntaje maximo entonces la actualiza
            PuntosAciertos.sos_pro(user["estadisticas"]["puntaje_maximo"],puntuacion_total,user["nombre"])
            #pone en 0 la casilla in game del usuario
            PuntosAciertos.clear_accumulated_points(user)
            PuntosAciertos.clear_accumulated_aciertos(user)
            print("Ganaste!")
            pass