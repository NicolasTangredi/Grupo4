import PySimpleGUI as sg

def build_config():
        layout =[[sg.Button( 'Cantidad de casillas', key='-CASILLAS-')],
                [sg.Button( 'Elemento', key='-ELEMENTO-')],
                [sg.Button( 'Cantidad de coincidencias', key='-COINCIDENCIAS-')],
                [sg.Button( 'Tiempo', key='-TIEMPO-')],
                [sg.Button( 'Paleta de colores', key='-COLOR-')],
                [sg.Button( 'Salir', key='-SALIR-')]]
        print('layout')
        window = sg.Window('Configuracion', layout)
        return window

def build_casillas():
    """contruye la ventana cantidad de casillas"""

    layout = [
        [sg.T("Elegi la cantidad de casillas")],
        [sg.Button('4x4', key='4x4')], 
        [sg.Button( '5x5', key='4x4')], 
        [sg.Button( '6x6', key='4x4')]
    ]

    window = sg.Window('Cantidad de casillas', layout)
    return window

def build_elemento():
    """contruye la ventana de elementos"""

    layout = [
        [sg.T("Elegi que tipo de elementos apareceran en la partida")],
        [sg.Button( 'palabras')], 
        [sg.Button( 'imagenes')]
    ]

    window = sg.Window('Tipo de elemento', layout)
    return window

def build_tiempo():

    """contruye la ventana de tiempo"""

    layout = [
        [sg.T("Elegi la duracion de la partida")],
        [sg.Button( '60')], 
        [sg.Button( '90')], 
        [sg.Button( '120')]
    ]
    window = sg.Window('Tiempo', layout)
    return window

def build_colores():
    """contruye la ventana de tiempo"""
    #hay que completar esto con los colores que pongamos
    layout = [[sg.T("Elegi la paleta de colores")],
        [sg.Button( 'Color1')], 
        [sg.Button( 'Color2')], 
        [sg.Button( 'Color3')]
    ]
    window = sg.Window('Paleta de colores', layout)
    return window

            
