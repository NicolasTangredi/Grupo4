import PySimpleGUI as sg


def build_estad(ganadas,perdidas,puntaje):
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.T("Partidas ganadas :"+ganadas)],
              [sg.T("Partidas perdidas : "+perdidas)],
              [sg.T("Mejor puntaje : "+puntaje)],
              [sg.Button("Ok")]]
    
    window = sg.Window('Estadisticas', layout) 
    return window
    