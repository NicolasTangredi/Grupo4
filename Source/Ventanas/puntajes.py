import PySimpleGUI as sg
from Source.Handlers import PuntosAciertos as PA

def build_punt():
    """ Construye la ventana del registro del usuario"""

    easy = PA.dividir_puntajes("facil")
    medium = PA.dividir_puntajes("medio")
    hard = PA.dividir_puntajes("dificil")
    #MAÑANA METO MAS JUGADORES XQ SINO ME REVIENTA LA VENTANA XD :]
    layout = [[sg.Text(hard[0][0]), sg.Text(hard[0][1]),sg.Text(hard[0][2])],
                [sg.Text(hard[1][0]), sg.Text(hard[1][1]),sg.Text(hard[1][2])],
                [sg.Text(hard[2][0]), sg.Text(hard[2][1]),sg.Text(hard[2][2])],
                [sg.Text(hard[3][0]), sg.Text(hard[3][1]),sg.Text(hard[3][2])],
                [sg.Text(hard[4][0]), sg.Text(hard[4][1]),sg.Text(hard[4][2])],
                [sg.Text(medium[0][0]), sg.Text(medium[0][1]),sg.Text(medium[0][2])],
                [sg.Text(medium[1][0]), sg.Text(medium[1][1]),sg.Text(medium[1][2])],
                [sg.Text(medium[2][0]), sg.Text(medium[2][1]),sg.Text(medium[2][2])],
                [sg.Text(medium[3][0]), sg.Text(medium[3][1]),sg.Text(medium[3][2])],
                [sg.Text(medium[4][0]), sg.Text(medium[4][1]),sg.Text(medium[4][2])],
                [sg.Text(easy[0][0]), sg.Text(easy[0][1]),sg.Text(easy[0][2])],
                [sg.Text(easy[1][0]), sg.Text(easy[1][1]),sg.Text(easy[1][2])],
                [sg.Text(easy[2][0]), sg.Text(easy[2][1]),sg.Text(easy[2][2])],
                [sg.Text(easy[3][0]), sg.Text(easy[3][1]),sg.Text(easy[3][2])],
                [sg.Text(easy[4][0]), sg.Text(easy[4][1]),sg.Text(easy[4][2])],
                [sg.Ok()]]

    window = sg.Window('Mejores puntajes por dificultad ', layout, element_justification='center') 
    return window         