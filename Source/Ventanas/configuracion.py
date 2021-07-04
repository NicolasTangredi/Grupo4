import PySimpleGUI as sg
from ..Handlers import usuario

def build_config():
        config = usuario.get_configuracion()
        cas = config['cant_casillas']
        coin = config['cant_coincidencias']
        tiempo = config['tiempo']
        elem = config ['tipo_elemento']
        layout =[
        [sg.Text ('Elegi la dificultad una dificultad predeterminada'), sg.Button('Facilito', key = '-FACIL-'), sg.Button('Normal', key = '-NORMAL-'), sg.Button('Goku no le gana', key = '-DIFICIL-')],
        [sg.Text('Cantidad de casillas'), sg.Text(cas, key = '-CASILLAS-')],
        [sg.Text('Tipo de elemento'), sg.Text(elem, key='-ELEMENTO-'), sg.Button('IMAGENES', key = '-ELEMENTO_IMAGENES-'), sg.Button('PALABRAS', key = '-ELEMENTO_PALABRAS-')],
        [sg.Text('Cantidad de coincidencias'), sg.Text(coin, key='-COIN-')],
        [sg.Text('Tiempo'), sg.Text(tiempo, key='-TIEMPO-')],
        [sg.Text('Paleta de Colores'), sg.Combo(["DarkTeal5","GreenTan"], key='-COLOR-'), sg.Text('(Es necesario reiniciar la aplicacion para cambiar los colores.')],
        [sg.Text('Si deja este campo vacio se utilizara una paleta de colores aleatoria)')], 
        [sg.Button('Save', key ='-SAVE-'), sg.Button ('Salir', key = '-SALIR-')]
        ]
        window = sg.Window('Configuracion', layout)
        return window


