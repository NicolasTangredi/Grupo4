import PySimpleGUI as sg
from Source.Handlers import elegir_datos

# recibiria x, y, criterio
def crear(user):
    ''' crea la ventana que funciona como el tablero del juego '''

    x = 5
    y = 5

    # datos = elegir_datos.elegir_criterio()
    # crit = datos['criterio'] 
    # pal = datos['data']
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
        margins = (3, 3)
    )
