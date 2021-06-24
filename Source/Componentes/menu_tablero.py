import traceback, PySimpleGUI as sg, time
from ..Handlers import timer, PuntosAciertos, datos_casilleros, usuario, clases, PuntosAciertos 
from ..Ventanas import tablero

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
    
    start_timer = time.time()

    while True:
        event, _value = window.read(timeout=100)

        if event == sg.WIN_CLOSED:
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
                sg.Popup("Ganaste!")
                break
            
        window["-TIMER-"].Update(timer.actualizar(start_timer))
        window.refresh()

        if(timer.se_termino_el_tiempo(start_timer, config["tiempo"])):
            jugada.finalizar()
            user = usuario.usuario_conectado_profile()
            PuntosAciertos.pro_o_manco(False,user["nombre"])
            sg.Popup("Se termino el tiempo")
            break
        

