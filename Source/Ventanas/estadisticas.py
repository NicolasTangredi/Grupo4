import PySimpleGUI as sg


def build_estad(ganadas,perdidas,puntaje):
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.T(f"Partidas ganadas : {ganadas}")],
              [sg.T(f"Partidas perdidas : {perdidas}")],
              [sg.T(f"Mejor puntaje : {puntaje}")],
              [sg.Button("Ok")]]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window
    