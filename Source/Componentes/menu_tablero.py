import traceback, PySimpleGUI as sg, time
from ..Handlers import timer, PuntosAciertos, datos_casilleros, usuario, clases, PuntosAciertos 
from ..Ventanas import tablero
import pygame as pg

def start():
    ''' comienza la ejecucion del tablero del juego'''
    
    user = usuario.usuario_conectado_profile()
    config, nombre = user['configuracion'], user['nombre']
    
    # esto es el alto y ancho del tablero y los datos
    x, y = tuple(map( int, config["cant_casillas"].split("x")))
    datos, crit = datos_casilleros.crearDatosJugada(config['tipo_elemento'], config['cant_coincidencias'], x, y)

    window = tablero.crear(nombre, crit)
    loop(window, datos, config, x, y)
    window.close()

def loop(window, datos, config, x, y):
    ''' loop de la ventana del tablero '''
    # crea los botones vacios e inicia la jugada
    coin = config["cant_coincidencias"]
    window.layout(datos_casilleros.crearCasillasVacias(x,y, coin))
    jugada = clases.Jugada(config, (x*y // coin))

    #configuro la musica de fondo y los efectos de sonido
    pg.mixer.init()
    pg.mixer.music.load('data/sonidos/background.mp3')
    pg.mixer.music.set_volume(0.01)
    derrota = pg.mixer.Sound('data/sonidos/maldicion.wav')
    victoria = pg.mixer.Sound('data/sonidos/victory.wav')
    victoria.set_volume(0.01)
    derrota.set_volume(0.01)
    #comienza la musica
    pg.mixer.music.play(-1)
    
    #guardo como referecia cuantos segundos pasaron desde una fecha en especifica
    start_timer = time.time()

    while True:
        event, _value = window.read(timeout=100)

        if event == sg.WIN_CLOSED:
            pg.mixer.music.stop()
            break

        if "CARD" in event:
            
            button = window[event]

            # consigue los valores de X e Y del boton (dato = -CARD-X,Y)
            x, y = event.split('-')[1].split(',')
            dato = datos[int(y)][int(x)]
            
            if config["tipo_elemento"] == 'imagenes':
                button.Update(image_data = dato, image_size=(100,102), disabled=True)  
            else: 
                button.Update(dato, disabled=True)
            
            window.refresh()
            fin = jugada.update(button, dato)

            if(fin):
                pg.mixer.music.stop()
                victoria.play()
                sg.Popup("Ganaste!")
                break
            
        window["-TIMER-"].Update(timer.actualizar(start_timer))
        window.refresh()

        if(timer.se_termino_el_tiempo(start_timer, config["tiempo"])):
            jugada.finalizar()
            pg.mixer.music.stop()
            derrota.play()
            user = usuario.usuario_conectado_profile()
            PuntosAciertos.pro_o_manco(False,user["nombre"])
            sg.Popup("Se termino el tiempo")
            break
        

