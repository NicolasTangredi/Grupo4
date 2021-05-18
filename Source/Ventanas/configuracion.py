import PySimpleGUI as sg

def build_config():
        layout =[[sg.Button( 'Cantidad de casillas', key='-CASILLAS-', size=(20,1))],
                [sg.Button( 'Elemento', key='-ELEMENTO-', size=(20,1))],
                [sg.Button( 'Cantidad de coincidencias', key='-COINCIDENCIAS-', size=(20,1))],
                [sg.Button( 'Tiempo', key='-TIEMPO-', size=(20,1))],
                [sg.Button( 'Paleta de colores', key='-COLOR-', size=(20,1))],
                [sg.Button( 'Salir', key='-SALIR-', size=(20,1))]]
        window = sg.Window('Configuracion', layout)
        return window

def build_casillas():
    """contruye la ventana cantidad de casillas"""

    layout = [
        [sg.T("Elegi la cantidad de casillas")],
        [sg.Button('4x4', key='4x4')], 
        [sg.Button( '5x5', key='5x5')], 
        [sg.Button( '6x6', key='6x6')]
    ]

    window = sg.Window('Cantidad de casillas', layout, element_justification='center')
    return window

def build_elemento():
    """contruye la ventana de elementos"""

    layout = [
        [sg.T("Elegi que tipo de elementos apareceran en la partida")],
        [sg.Button( 'palabras')], 
        [sg.Button( 'imagenes')]
    ]

    window = sg.Window('Tipo de elemento', layout, element_justification='center')
    return window

def build_tiempo():

    """contruye la ventana de tiempo"""

    layout = [
        [sg.T("Elegi la duracion de la partida")],
        [sg.Button( '60', key = "-60-")], 
        [sg.Button( '90', key = "-90-")], 
        [sg.Button( '120', key = "-120-")]
    ]
    window = sg.Window('Tiempo', layout, element_justification='center')
    return window

def build_colores():
    """contruye la ventana de tiempo"""
    #hay que completar esto con los colores que pongamos
    layout = [[sg.T("Elegi la paleta de colores")],
        [sg.Button( 'Color1')], 
        [sg.Button( 'Color2')], 
        [sg.Button( 'Color3')]
    ]
    window = sg.Window('Paleta de colores', layout, element_justification='center')
    return window

def build_coincidencias():

    """contruye la ventana de coincidencias"""

    layout = [
        [sg.T("Elegi la cantidad de coincidencias")],
        [sg.Button( 'Cant1', key = "-1-")], 
        [sg.Button( 'Cant2', key = "-2-")], 
        [sg.Button( 'Cant3', key = "-3-")]
    ]
    window= sg.Window('Coincidencias', layout, element_justification='center')
    return window

            
