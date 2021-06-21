import PySimpleGUI as sg
from Source.Handlers import usuario

def build_punt():
    """ Construye la ventana del registro del usuario"""

    lista = usuario.dame_puntuaciones_pa()

    llaves = list(usuario.dame_puntuaciones_pa().keys())
    valores = list(usuario.dame_puntuaciones_pa().values())
    dificultad = usuario.dif_usuarios()
        
    layout = [[sg.Text(llaves[0]), sg.Text(valores[0]),sg.Text(dificultad[llaves[0]])],
                [sg.Text(llaves[1]), sg.Text(valores[1]),sg.Text(dificultad[llaves[1]])],
                [sg.Text(llaves[2]), sg.Text(valores[2]),sg.Text(dificultad[llaves[2]])],
                [sg.Text(llaves[3]), sg.Text(valores[3]),sg.Text(dificultad[llaves[3]])],
                [sg.Text(llaves[4]), sg.Text(valores[4]),sg.Text(dificultad[llaves[4]])],
                [sg.Text(llaves[5]), sg.Text(valores[5]),sg.Text(dificultad[llaves[5]])],
                [sg.Text(llaves[6]), sg.Text(valores[6]),sg.Text(dificultad[llaves[6]])],
                [sg.Text(llaves[7]), sg.Text(valores[7]),sg.Text(dificultad[llaves[7]])],
                [sg.Text(llaves[8]), sg.Text(valores[8]),sg.Text(dificultad[llaves[8]])],
                [sg.Text(llaves[9]), sg.Text(valores[9]),sg.Text(dificultad[llaves[9]])],
                [sg.Ok()]]

    window = sg.Window('los 3 Mejores puntajes ', layout, element_justification='center') 
    return window         