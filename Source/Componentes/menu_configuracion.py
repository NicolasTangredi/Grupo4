import PySimpleGUI as sg
from Source.Ventanas import configuracion
from Source.Handlers import config
from Source.Handlers import usuario


def start():
    """Ejecuta la ventana del menu de configuracion"""
    window = configuracion.build_config()
    loop(window)
    window.close()



def loop(window):
    """crea la ventana de configuracion"""
    user = usuario.usuario_conectado()
    guarde = False
    while True:
        event, values = window.read()

        if (event == '-SALIR-') or (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
            if guarde:
                pop1 = sg.popup_yes_no('Estas segurx que queres salir?')
                if pop1 == 'Yes':
                    break
            else:
                pop2= sg.popup_yes_no('Estas segurx que queres salir sin guardar los cambios?')         
                if pop2 == 'Yes':
                    break
                
        elif event == "-FACIL-":
            window['-CASILLAS-'].update("4x4")
            window['-ELEMENTO-'].update("imagenes")
            window['-COIN-'].update(2)
            window['-TIEMPO-'].update(120)
            window['-COLOR-'].update("DarkTeal5")
        elif event == "-NORMAL-":
            window['-CASILLAS-'].update("5x5")
            window['-ELEMENTO-'].update("imagenes")
            window['-COIN-'].update(2)
            window['-TIEMPO-'].update(90)
            window['-COLOR-'].update("DarkTeal5")
        elif event == "-DIFICIL-":
            window['-CASILLAS-'].update("6x6")
            window['-ELEMENTO-'].update("imagenes")
            window['-COIN-'].update(3)
            window['-TIEMPO-'].update(60)
            window['-COLOR-'].update("DarkTeal5")

        elif event == '-ELEMENTO_IMAGENES-':
            window['-ELEMENTO-'].update("imagenes")
        elif event == '-ELEMENTO_PALABRAS-':
            window['-ELEMENTO-'].update("palabras")
                 
        elif event == '-SAVE-':
     
            valores = {'cant_casillas' : window['-CASILLAS-'].get(),
                        'tipo_elemento': window['-ELEMENTO-'].get(),
                        'cant_coincidencias': int(window['-COIN-'].get()),
                        'tiempo': int(window['-TIEMPO-'].get()),
                        'paleta_de_colores': values['-COLOR-']}
            print('pase el save')
            config.set_config(valores,user)
            
    return window           





