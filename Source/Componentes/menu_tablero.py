import PySimpleGUI as sg
from ..Ventanas import tablero

def start(user):
    ''' comienza la ejecucion del tablero del juego'''
    
    window = tablero.crear(user)
    loop(window)
    window.close()

def loop(window):
    
    while True:
        event, _value = window.read()

        if event == sg.WIN_CLOSED:
            break