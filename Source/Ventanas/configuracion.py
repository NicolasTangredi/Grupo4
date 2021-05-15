import PySimpleGUI as sg

def build_config():
        
        layout =[[sg.button( 'Cantidad de casillas', '-CASILLAS-')],
                [sg.button( 'Elemento', '-ELEMENTO-')],
                [sg.button( 'Cantidad de coincidencias', '-COINCIDENCIAS-')],
                [sg.button( 'Tiempo', '-TIEMPO-')],
                [sg.button( 'Paleta de colores', '-COLOR-')],
                [sg.button( 'Salir', '-SALIR-')]]
        window = sg.Window('Configuracion', layout)
        return window

def build_casillas():
    """contruye la ventana cantidad de casillas"""

    layout = [[sg.T("Elegi la cantidad de casillas")]
            [sg.button( '4x4')], [sg.button( '5x5')], [sg.button( '6x6')]]
    window = sg.Window('Cantidad de casillas', layout)
    return window

def build_elemento():
    """contruye la ventana de elementos"""

    layout = [[sg.T("Elegi que tipo de elementos apareceran en la partida")]
            [sg.button( 'palabras')], [sg.button( 'imagenes')]]
    window = sg.Window('Tipo de elemento', layout)
    return window

def build_tiempo():

    """contruye la ventana de tiempo"""

    layout = [[sg.T("Elegi la duracion de la partida")]
            [sg.button( '60')], [sg.button( '90')], [sg.button( '120')]]
    window = sg.Window('Tiempo', layout)
    return window

def build_colores():
    """contruye la ventana de tiempo"""
    #hay que completar esto con los colores que pongamos
    layout = [[sg.T("Elegi la paleta de colores")]
            [sg.button( 'Color1')], [sg.button( 'Color2')], [sg.button( 'Color3')]]
    window = sg.Window('Paleta de colores', layout)
    return window

            
