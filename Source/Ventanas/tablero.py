import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

# recibiria x, y, criterio
def crear():
    ''' crea la ventana que funciona como el tablero del juego '''

    x = 8
    y = 8
    criterio = 'Gimnastas olimpicos que participaron en las olimpiadas en Atenas'

    layout = [
        [sg.Text('Criterio: ' + criterio)],
    ]

    # genera X botones en Y filas para crear el tablero
    filas = []
    for _i in range(y):
        fila = []
        for _i in range(x):
            fila.append(sg.Button('palabra', size=(8, 4)))
        filas.append(fila)
    
    layout = layout + filas

    return sg.Window(
        'tablero',
        layout,
        element_justification = 'center',
        margins = (3,3)
    )
