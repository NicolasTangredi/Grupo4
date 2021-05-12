import PySimpleGUI as sg

def crear():
    ''' crea y devuelve la ventana del menu principal '''

    button = lambda txt, key: sg.Button(txt, key= key, size=(20, 2))
    layout = [
        [sg.Text("MEM-PY", font=('', 30), pad=(3, 5))],
        [button( 'Jugar', '-JUGAR-')],
        [button( 'Opcion', '-OPCION-')],
        [button( 'Puntos', '-PUNTOS-')],
        [button( 'Estadisticas', '-ESTAD-')],
        [button( 'Salir', '-SALIR-')]
    ]

    return sg.Window(
        'Mem-Py, juego de la memoria',
        margins = (50, 5),
        element_justification = 'center',
        layout = layout)
    