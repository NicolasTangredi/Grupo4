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

        if event == '-SALIR-':
            if guarde:
                pop1 = sg.popup_yes_no('Estas segurx que queres salir?')
                if pop1 == 'Yes':
                    break
            else:
                pop2= sg.popup_yes_no('Estas segurx que queres salir sin guardar los cambios?')         
                if pop2 == 'Yes':
                    break
                
        elif event == None:
            sg.popup('No se guardaron los cambios')
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
             window['-COIN-'].update(2)
             window['-TIEMPO-'].update(60)
             window['-COLOR-'].update("DarkTeal5")
        elif event == '-SAVE-':
            guarde = True
            valores = {'cant_casillas' : values['-CASILLAS-'], 'tipo_elemento': values['-ELEMENTO-'], 'cant_coincidencias': values['-COIN-'], 'tiempo': values['-TIEMPO-'], 'paleta_de_colores':values['-COLOR-']}
            config.set_config(valores,user)
            
    return window           





