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
    "Construye la ventana que lleva el grafico de cantidad de partidas finalizadas,abandonadas y timeout"
    
    layout = [[sg.Image("grafico.png")],
              [sg.Button("Ok")]
              ]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window
    

def build_graph2():
    "Construye la ventana que lleva los porcentajes de partidas finalizadas por genero"
    
    layout = [[sg.Image("grafica.png")],
              [sg.Button("Ok")]]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window

def build_estad3():
    "Construye la ventana que lleva el top 10 de palabras que primero se encontaron"
    top10 = st.convertirTop()
    top10 = [[f"Top {top10.index(li) + 1}"] + li for li in top10]

    layout = [
        [sg.Table(
            values=top10,
            headings=["Posicion", "Palabra", "Cant"],
            num_rows=len(top10),
            auto_size_columns = True,
            justification = 'center',
            alternating_row_color = 'lightblue',
            hide_vertical_scroll = True,
            size=(200, 300)
        )],
        [sg.Button("Ok")]
    ]
    
    window = sg.Window('Palabras primero encontradas', layout) 
    return window
    