import PySimpleGUI as sg
from Source.Handlers import PuntosAciertos as PA

def build_punt():
    """ Construye la ventana del registro del usuario"""

    easy = PA.dividir_puntajes("facil")
    medium = PA.dividir_puntajes("medio")
    hard = PA.dividir_puntajes("dificil")
    
    # En caso de que haya menos de 5 jugadores este trozo de codigo colocara la cantidad que haya
    # y evitara el cierre de la ventana
    var = []
    cant = len(hard)
    for i in range(0,cant):
        var.append([sg.Text(hard[i][0]), sg.Text(hard[i][1]),sg.Text(hard[i][2])])
        
    var2 = []
    cant2 = len(medium)
    for h in range(0,cant2):
        var2.append([sg.Text(medium[h][0]), sg.Text(medium[h][1]),sg.Text(medium[h][2])])
        
    var3 = []
    cant3 = len(easy)
    for k in range(0,cant3):
        var3.append([sg.Text(easy[k][0]), sg.Text(easy[k][1]),sg.Text(easy[k][2])])
        
    layout = [var,
               var2,
                 var3,
                [sg.Ok()]]

    window = sg.Window('Mejores puntajes por dificultad ', layout, element_justification='center') 
    return window         