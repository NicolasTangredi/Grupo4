import PySimpleGUI as sg


def build_estad():
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.T("Porcentaje de partidas abandonadas,finalizadas y timeout")],
              [sg.Button("a ver pa")],
                [sg.T("Porcentaje de partidas finalizadas por genero")],
                [sg.Button("mostra compa")],
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
    

def build_graph2():
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.Image("grafica.png")],
              [sg.Button("Ok")]]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window
    