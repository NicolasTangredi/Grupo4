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
    window = estadisticas.build_estad()

    while True:
        event, _values = window.read()
        
        if event == "a ver pa":
            st.porcentaje()
            start2()
            break
        
        if event == "mostra compa":
            st.porcentaje2()
            start3()
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

def start3():
    "Ejecuta la ventana de estadisticas del menu principal "

    window = loop3()
    window.close()
    
def loop3():
    window = estadisticas.build_graph2()

    while True:
        event, _values = window.read()
         
        if event == "Ok" or event == None:
            break
        
    return window
            