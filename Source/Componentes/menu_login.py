import PySimpleGUI as sg
from Source.Ventanas import ventana_login
from Source.Componentes import menu_signin
from Source.Handlers import usuario

def start():
    """Ejecuta la ventana del menu de inicio de sesion"""

    window = loop()
    window.close()


def loop():
    """ Mantiene 'viva' la ventana """
    window = ventana_login.build_login()
    while True:
        event, values = window.read()

        if event == None or event == "Cancel":
            break
        
        if event == "LogIn":
            user = values["-USER-"]
            pwd = values["-PASS-"]

            try:
                users = usuario.usuarios_registrados()
                if user not in users:
                    window_aviso = ventana_login.build_no_registrado()
                    while True:
                        event2 = window_aviso.read()
                        if event2 == None or event == 'Ok':
                            break
                



            except:
                users = []
                        
        if event == 'Registrarse':
            window.hide()
            menu_signin.start()
            window.un_hide()

    return window    

