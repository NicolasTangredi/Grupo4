import PySimpleGUI as sg
from ..Handlers import stats as st


def build_estad():
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.T("Porcentaje de partidas abandonadas,finalizadas y timeout")],
              [sg.Button("a ver pa")],
              [sg.T("Porcentaje de partidas finalizadas por genero")],
              [sg.Button("mostra compa")],
              [sg.T("Top 10 palabras primero encontradas en todas las partidas")],
              [sg.Button("KIERO BER")],
              [sg.T("                 ")],
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

def build_estad3():
    "Construye la ventana de estadisticas del usuario"
    top10 = st.convertirTop()
    
    layout = [[sg.T("Top 1")],[sg.T(top10[0][0])],[sg.T(top10[0][1])],[sg.T("                ")],
              [sg.T("Top 2")],[sg.T(top10[1][0])],[sg.T(top10[1][1])],[sg.T("                ")],
              [sg.T("Top 3")],[sg.T(top10[2][0])],[sg.T(top10[2][1])],[sg.T("                ")],
              [sg.T("Top 4")],[sg.T(top10[3][0])],[sg.T(top10[3][1])],[sg.T("                ")],
              [sg.T("Top 5")],[sg.T(top10[4][0])],[sg.T(top10[4][1])],[sg.T("                ")],
              [sg.Button("Ok")]
              ]
    
    window = sg.Window('Palabras primero encontradas', layout) 
    return window
    