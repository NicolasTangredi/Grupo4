import PySimpleGUI as sg
from ..Ventanas import principal as ventana
from ..Componentes import menu_estadisticas 

def iniciar():

    window = ventana.crear()
    loop(window)
    
def loop(window):

    while True:
        event, _value = window.read()

        if(event == '-JUGAR-'):
            print('jugando')
            window.hide()
            # agregar menu tablero aca
            window.un_hide()
        
        elif(event == '-OPCION-'):
            print('opciones')
            window.hide()
            # agregar menu opciones aca
            window.un_hide()
        
        elif(event == '-PUNTOS-'):
            print('puntajes')
            window.hide()
            menu_puntajes()
            window.un_hide()

        elif(event == '-ESTAD-'):
            print('estadisticas')
            window.hide()
            menu_estadisticas()
            window.un_hide()

        elif(event == '-SALIR-' or event == sg.WIN_CLOSED):
            window.close()
            break
        
