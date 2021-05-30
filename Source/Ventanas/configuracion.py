import PySimpleGUI as sg

def build_config():
        layout =[
        [sg.Text ('Elegi la dificultad una dificultad predeterminada'), sg.Button('Facilito', key = '-FACIL-'), sg.Button('Normal', key = '-NORMAL-'), sg.Button('Goku no le gana', key = '-DIFICIL')],
        [sg.Text('O usa una configuracion personalizada:')],
        [sg.Text('Cantidad de casillas'),  sg.Combo(['4x4','5x5','6x6'], key='-CASILLAS-')],
        [sg.Text('Tipo de elemento'), sg.Combo(['palabras', 'imagenes'], key='-ELEMENTO-')],
        [sg.Text('Cantidad de coincidencias'), sg.Combo([1,2,3], key='-COIN-')],
        [sg.Text('Tiempo'), sg.Combo([60,90,120], key='-TIEMPO-')],
        [sg.Text('Paleta de Colores'), sg.Combo(["DarkTeal5","GreenTan"], key='-COLOR-')], 
        [sg.Button('Save', key ='-SAVE-'), sg.Button ('Salir', key = '-SALIR-')]
        ]
        window = sg.Window('Configuracion', layout)
        return window


