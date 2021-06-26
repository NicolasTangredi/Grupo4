import PySimpleGUI as sg, time, os
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
    try:
        window = tablero.crear(nombre, crit)
        loop(window, datos, config, x, y)
        window.close()
    except Exception as err:
        print(err)

def loop(window, datos, config, x, y):
    ''' loop de la ventana del tablero '''
    coin = config["cant_coincidencias"]
    buttons = datos_casilleros.crearCasillasVacias(x, y, coin)
    window.layout(buttons)
    window.finalize()

    #configuro la musica de fondo y los efectos de sonido
    pg.mixer.init()
    pg.mixer.music.load('data/sonidos/background.wav')
    pg.mixer.music.set_volume(0.01)
    derrota = pg.mixer.Sound('data/sonidos/maldicion.wav')
    victoria = pg.mixer.Sound('data/sonidos/victory.wav')
    
    victoria.set_volume(0.01)
    derrota.set_volume(0.01)
    
    #comienza la musica
    pg.mixer.music.play(-1)

    for rows in buttons: 
        for elem in rows: elem.Update("", disabled=True)
    event, _value = window.read()
    
    if event == "-JUGAR-":
        # crea una jugada, los botones vacios y empieza el timer
        for rows in buttons: 
            for elem in rows: elem.Update("", disabled=False)
        
        window['-JUGAR-'].Update("Pausa")

        start_timer = time.time()
        jugada = clases.Jugada(config, (x * y // coin))

        while True:
            event, _value = window.read(timeout=100)
            tiempo = timer.actualizar(start_timer)

            if event == sg.WIN_CLOSED:
                jugada._registrar_jugada('fin', jugada._numJug,"abandonada")
                pg.mixer.music.stop()
                break

            if event == "-JUGAR-":
                start_timer += timer.parar()

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
                fin = jugada.update(button, dato, tiempo)

                if(fin):
                    jugada._registrar_jugada('fin', jugada._numJug,"finalizada")
                    pg.mixer.music.stop()
                    victoria.play()
                    mostrar_mensaje('Ganaste!', 'Conseguiste todas las coincidencias', "Win.gif")
                    break
                
            window["-TIMER-"].Update('Tiempo:' f'{round(tiempo // 60):02d}:{round(tiempo % 60):02d}')
            window.refresh()

            if(timer.se_termino_el_tiempo(start_timer, config["tiempo"])):
                jugada._registrar_jugada('fin', jugada._numJug,"timeout",tiempo)
                jugada.finalizar()
                
                pg.mixer.music.stop()
                derrota.play()

                user = usuario.usuario_conectado_profile()
                PuntosAciertos.pro_o_manco(False,user["nombre"])
                
                mostrar_mensaje('perdiste', 'se te acabo el tiempo', "Lose.gif")
                break
    else:
        pg.mixer.music.stop()
        

def mostrar_mensaje(titulo, mensaje, name_img):
    """ muestra un mensaje al usuario con un gif,
        del gif solo se necesita el nombre del archivo con la extension
    """      
    layout = [   
        [sg.Text(mensaje, font=('', 15))],
        [sg.Image(key="-GIF-", filename=os.path.join('data/imagenes', name_img))],
        [sg.Ok(size=(12,2))]
    ]
    
    window = sg.Window(titulo, layout, element_justification="center")
    
    while True:
        event, _value = window.read(timeout=20)
        window["-GIF-"].update_animation(
            os.path.join('data/imagenes', name_img),
            time_between_frames=20
        )
        
        if event == "Ok" or event == sg.WIN_CLOSED:
            window.close()
            break