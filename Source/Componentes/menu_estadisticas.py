import PySimpleGUI as sg
from os import remove
from Source.Ventanas import estadisticas
from Source.Handlers import usuario
from ..Handlers import stats as st
from matplotlib import pyplot as pt


def start():
    "Ejecuta la ventana de estadisticas del menu principal "

    window = loop()
    window.close()
    
def loop():
    num1,num2,num3 = usuario.stats_logged()
    window = estadisticas.build_estad(num1,num2,num3)

    while True:
        event, _values = window.read()
        
        if event == "a ver pa":
            st.porcentaje()
            start2()
            break
        
        if event == "Ok" or event == None:
            break
        
    return window

def start2():
    "Ejecuta la ventana de estadisticas del menu principal "

    window = loop2()
    window.close()
    
def loop2():
    window = estadisticas.build_graph1()

    while True:
        event, _values = window.read()
         
        if event == "Ok" or event == None:
            break
        
    return window
            