import PySimpleGUI as sg
from Source.Handlers import PuntosAciertos as PA

def build_punt():
    """ Construye la ventana del registro del usuario"""
    easy = PA.dividir_puntajes("facil")
    medium = PA.dividir_puntajes("medio")
    hard = PA.dividir_puntajes("dificil")  
    
    rows = len(max([easy, medium, hard], key=len))
    def create_table(data, dif):
        return sg.Table(
            values = data,
            headings = [dif, "Puntos"],
            auto_size_columns = True,
            justification = 'center',
            alternating_row_color = 'lightblue',
            hide_vertical_scroll = True,
            num_rows = rows
        )
    layout = [
        [   create_table(easy if (len(easy) > 0) else ["Vacio", ""], "Facil"),
            create_table(medium if (len(medium) > 0) else ["vacio", ""], "Medio"),
            create_table(hard if (len(hard) > 0) else ["vacio", ""], "Dificil")
        ],
        [sg.Ok()]
    ]

    window = sg.Window('Mejores puntajes por dificultad ', layout, element_justification='center') 
    return window
      