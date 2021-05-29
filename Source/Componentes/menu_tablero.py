import json, PySimpleGUI as sg
from ..Ventanas import tablero
from ..Handlers import datos_casilleros, usuario

def start():
    ''' comienza la ejecucion del tablero del juego'''
    
    nombre = usuario.usuario_conectado()
    config = None
    with open("data/usuarios.json","r", encoding="utf8") as file:
        users = json.load(file)
        user = [user for user in users if user["nombre"] == nombre][0]
        config = user['configuracion']

    x, y = tuple(map( int, config["cant_casillas"].split("x")))

    datos, crit = datos_casilleros.crearDatosJugada(config['tipo_elemento'], config['cant_coincidencias'], x, y)
    
    window = tablero.crear(nombre, crit)
    print('hola')
    loop(window, datos, config['tipo_elemento'], x, y)
    window.close()
        
def loop(window, datos, tipo, x, y):
    window.layout(datos_casilleros.crearCasillasVacias(x,y))

    while True:
        event, _value = window.read()
        print(event)
        
        realEv, values = event.split('-')
        if realEv == "CARD":
            button = window[event]
            
            x, y = values.split(',')
            dato = datos[int(y)][int(x)]
            button.Update(image_data=dato) if tipo == 'imagenes' else button.Update(dato)

        if event == sg.WIN_CLOSED:
            break