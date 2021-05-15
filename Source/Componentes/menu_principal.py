import PySimpleGUI as sg
from ..Ventanas import principal as ventana
from ..Componentes import menu_estadisticas, menu_tablero 
from ..Componentes import menu_puntajes
from ..Componentes import menu_configuracion
from ..Handlers import usuario

def iniciar():
    ''' comienza la ejecucion del menu del juego '''

    window = ventana.crear()
    loop(window)
    
def loop(window):
    ''' mantiene la ventana abierta y recibe el input del usuario '''
    
    while True:
        event, _value = window.read()

        if(event == '-JUGAR-'):
            window.hide()
            menu_tablero.start()
            window.un_hide()
        
        elif(event == '-CONFIG-'):
            print('configuracion')
            window.hide()
            menu_configuracion.start()
            window.un_hide()
        
        elif(event == '-PUNTOS-'):
            window.hide()
            menu_puntajes.start()
            window.un_hide()

        elif(event == '-ESTAD-'):
            print('estadisticas')
            window.hide()
            menu_estadisticas.start()
            window.un_hide()

        elif(event == '-SALIR-' or event == sg.WIN_CLOSED):
            user = usuario.usuario_conectado()
            usuario.user_disconnected(user)
            window.close()
            break
        
