import PySimpleGUI as sg
from Source.Ventanas import configuracion
from Source.Handlers import config
from Source.Handlers import usuario


def start():
    """Ejecuta la ventana del menu de configuracion"""
    window = configuracion.build_config()
    loop(window)
    window.close()



def loop(window):
    """crea la ventana de configuracion"""
    user = usuario.usuario_conectado()
    while True:
        event, values = window.read()


        if event == None or event == "-SALIR-":
            break
        
        elif event == "-CASILLAS-":
            window.hide()
            menu_casillas(user)
            window.un_hide()

        elif event == "-ELEMENTO-":
            window.hide()
            menu_elemento(user)
            window.un_hide()

        elif event == "-COINCIDENCIAS-":
            window.hide()
            menu_coincidecncias(user)
            window.un_hide()

        elif event == "-TIEMPO-":
            window.hide()
            menu_tiempo(user)
            window.un_hide()

        elif event == "-COLOR-":
            window.hide()
            menu_color(user)
            window.un_hide()
    return window           


def menu_casillas(user):
    """ejecuta la ventana de configuracion de casillas"""
    
    window = configuracion.build_casillas()
    while True:
        event, values = window.read()
        if event == None:
            break
        elif event == "4x4":
            config.set_config("cant_casillas","4x4",user)
            break
        elif event == "5x5":
            config.set_config("cant_casillas","5x5",user)
            break
        elif event == "6x6":
            config.set_config("cant_casillas","6x6",user)
            break
    window.close()    

def menu_elemento(user):
    """ejecuta la ventana de configuracion de elementos"""

    window = configuracion.build_elemento()
    while True:
        event, values = window.read()
        if event == None:
            break
        elif event == "palabras":
            config.set_config("tipo_elemento","palabras",user)
            break
        elif event == "imagenes":
            config.set_config("tipo_elemento","imagenes",user)
            break
    window.close()


def menu_tiempo(user):
    """ejecuta la ventana de configuracion del tiempo"""

    window = configuracion.build_tiempo()
    while True:
        event, values = window.read()
        if event == None:
            break
        elif event == "-60-":
            config.set_config("tiempo",60,user)
            break
        elif event == "-90-":
            config.set_config("tiempo",90,user)
            break
        elif event == "-120-":
            config.set_config("tiempo",120,user)
            break
    window.close()

def menu_color(user):
    """ejecuta la ventana de configuracion del tiempo"""

    window = configuracion.build_colores()
    while True:
        event, values = window.read()
        if event == None:
            break
        elif event == "Color1":
            config.set_config("paleta_de_colores","Color1",user)
            break
        elif event == "Color2":
            config.set_config("paleta_de_colores","Color2",user)
            break
        elif event == "Color3":
            config.set_config("paleta_de_colores","Color3",user)
            break
    window.close()

def menu_coincidecncias(user):
    """ejecuta la ventana de configuracion de coincidencias"""
    
    window = configuracion.build_coincidencias()
    while True:
        event, values = window.read()
        if event == None:
            break
        elif event == "-1-":
            config.set_config("cant_coincidencias","Cant1",user)
            break
        elif event == "-2-":
            config.set_config("cant_coincidencias","Cant2",user)
            break
        elif event == "-3-":
            config.set_config("cant_coincidencias","Cant3",user)
            break
    window.close()                    
           
                



