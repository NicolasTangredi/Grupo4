import PySimpleGUI as sg
import time as t
from ..Handlers import timer
from ..Handlers import PuntosAciertos
from ..Ventanas import tablero
from ..Handlers import datos_casilleros, usuario, clases
from ..Handlers import PuntosAciertos

def start():
    ''' comienza la ejecucion del tablero del juego'''
    
    user = usuario.usuario_conectado_profile()
    config, nombre = user['configuracion'], user['nombre']

    # esto es el alto y ancho del tablero y los datos
    x, y = tuple(map( int, config["cant_casillas"].split("x")))
    datos, crit = datos_casilleros.crearDatosJugada(config['tipo_elemento'], config['cant_coincidencias'], x, y)
        
    window = tablero.crear(nombre, crit)
    loop(window, datos, config['tipo_elemento'], config['cant_coincidencias'], x, y)
    window.close()

def loop(window, datos, tipo, coin, x, y):
    ''' loop de la ventana del tablero '''
    #Reinicia sus aciertos y puntos en caso de que se haya cerrado inesperadamente la partida anterior y quedaran guardados
  #  if PuntosAciertos.puntuacion_acumulada() != 0:
   #     PuntosAciertos.clear_accumulated_aciertos()
   # if PuntosAciertos.aciertos() != 0:    
   #     PuntosAciertos.clear_accumulated_points()
    # crea los botones vacios e inicia la jugada
    window.layout(datos_casilleros.crearCasillasVacias(x,y, coin))
    jugada = clases.Jugada(tipo, coin, (x*y // coin))
    
    start_timer = t.time()
    while True:
        event, _value = window.read()

        if event == sg.WIN_CLOSED:
            break

        realEv, values = event.split('-')

        if realEv == "CARD":
            button = window[event]

            # consigue los valores de x e y del boton, busca el dato adecuado y actualiza
            x, y = values.split(',')
            dato = datos[int(y)][int(x)]
            button.Update(image_data=dato, image_size=(100,102), disabled=True) if tipo == 'imagenes' else button.Update(dato, disabled=True)
            window.refresh()
            evento = jugada.update(button, dato)
        #window["-TIMER-"].Update(timer.actualizar(start_timer))
        #window.refresh()
