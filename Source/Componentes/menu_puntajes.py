import PySimpleGUI as sg
from Source.Ventanas import puntajes

def start():
    """Ejecuta la ventana de puntajes del menu principal"""

    window = loop()
    window.close()


def loop():

    window = puntajes.build_punt()
     
            
    while True:
        event,values = window.read()
        
        if event == "Ok" or event == sg.WIN_CLOSED:
            break      
                    
    return window        