import PySimpleGUI as sg
from Source.Ventanas import estadisticas
from Source.Handlers import usuario

def start():
    "Ejecuta la ventana de estadisticas del menu principal "

    window = loop()
    window.close()
    
def loop():
    num1,num2,num3 = usuario.stats_logged()
    window = estadisticas.build_estad(num1,num2,num3)

    while True:
        event, _values = window.read()
        
        if event == "Ok" or event == None:
            break
    return window
            