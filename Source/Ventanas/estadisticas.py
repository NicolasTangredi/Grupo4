import PySimpleGUI as sg


def build_estad(ganadas,perdidas,puntaje):
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.T("Porcentaje de partidas abandonadas,finalizadas y timeout")],
              [sg.Button("a ver pa")],
              [sg.Button("Ok")]
              ]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window

def build_graph1():
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.Image("grafico.png")],
              [sg.Button("Ok")]
              ]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window
    