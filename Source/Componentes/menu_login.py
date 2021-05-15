import PySimpleGUI as sg
from Source.Ventanas import login
from Source.Componentes import menu_signin, menu_principal
from Source.Handlers import usuario
from Source.Ventanas import avisos

def start():
    """Ejecuta la ventana del menu de inicio de sesion"""

    loop()


def loop():
    """ Mantiene 'viva' la ventana """
    window = login.build_login()
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
                    sg.popup('usuario no registrado')
                elif not usuario.check_contra(user,pwd):
                    sg.popup('contraseña incorrecta')
                else:
                    window.close()
                    usuario.user_logged(user,pwd)
                    menu_principal.iniciar()
                    break        
            except:
                users = []
                        
        if event == 'Registrarse':
            window.hide()
            menu_signin.start()
            window.un_hide()

    return window    

