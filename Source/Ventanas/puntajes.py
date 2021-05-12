import PySimpleGUI as sg
from Source.Handlers import usuario

def build_punt():
    """ Construye la ventana del registro del usuario"""

    lista = usuario.max_punt() 
        
    layout = [[sg.Text(lista[0]), sg.Text(lista[1])],
                [sg.Text(lista[2]), sg.Text(lista[3])],
                [sg.Text(lista[4]), sg.Text(lista[5])],
                [sg.Ok()]]

    window = sg.Window('los 3 Mejores puntajes ', layout) 
    return window         