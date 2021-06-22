import json, PySimpleGUI as sg
import time as t
from ..Ventanas import tablero
from ..Handlers import datos_casilleros, usuario, clases, timer

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

                