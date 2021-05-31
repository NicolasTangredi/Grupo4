import json, PySimpleGUI as sg
from time import sleep
from ..Ventanas import tablero
from ..Handlers import datos_casilleros, usuario, clases

def start():
    ''' comienza la ejecucion del tablero del juego'''
    
    nombre = usuario.usuario_conectado()
    config = None
    with open("data/usuarios.json","r", encoding="utf8") as file:
        users = json.load(file)
        user = [user for user in users if user["nombre"] == nombre][0]
        config = user['configuracion']

    # esto es el alto y ancho del tablero y los datos
    x, y = tuple(map( int, config["cant_casillas"].split("x")))
    datos, crit = datos_casilleros.crearDatosJugada(config['tipo_elemento'], config['cant_coincidencias'], x, y)
        
    window = tablero.crear(nombre, crit)
    loop(window, datos, config['tipo_elemento'], config['cant_coincidencias'], x, y)
    window.close()

def loop(window, datos, tipo, coin, x, y):
    ''' loop de la ventana del tablero '''

    # crea los botones vacios e inicia la jugada
    window.layout(datos_casilleros.crearCasillasVacias(x,y))
    jugada = clases.Jugada(coin)

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
            button.Update(image_data=dato, disabled=True) if tipo == 'imagenes' else button.Update(dato, disabled=True)
            evento = jugada.update(button, dato)

            # manejaria los eventos del juego
            if(not evento == None):
                if(not evento):
                    window.refresh()
                    sleep(0.5)
                    jugada.mala(tipo)