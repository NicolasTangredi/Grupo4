from base64 import encode
import json, io, random, requests, PySimpleGUI as sg
from Source.Handlers import elegir_datos
from Source.Handlers import usuario
from PIL import Image

# recibiria x, y, criterio
def crear(nombre, dificultad, crit):
    '''crea la ventana que funciona como el tablero del juego'''

    layout = [
        [sg.Text(f'Criterio: {crit}')],
        [   sg.Button('Comenzar', key="-JUGAR-"), 
            sg.Text(f'dificultad: {dificultad}'), 
            sg.Text(f'Jugador: {nombre}'), 
            sg.Text('Puntos: 000', key="-PUNT-"),
            sg.Text('Tiempo: 00:00', key='-TIMER-')
        ]
    ]
    
    return sg.Window(
        'tablero',
        layout,
        element_justification = 'center',
        margins = (3, 3),
        enable_close_attempted_event= True
    )
