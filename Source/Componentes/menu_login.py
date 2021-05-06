import PySimpleGUI as sg
from Source.Ventanas import login
from Source.Componentes import menu_signin
from Source.Handlers import usuario
from Source.Ventanas import avisos

def start():
    """Ejecuta la ventana del menu de inicio de sesion"""

    window = loop()
    window.close()

def crear_aviso(funcion):
    window = funcion
    while True:
        event = window.read()
        if event == None or event == 'Ok':
            break 
    return window

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
                    window.hide()
                    crear_aviso(avisos.build_no_registrado())
                    loop()
                if not usuario.check_contra(user,pwd):
                    crear_aviso(avisos.build_contra_incorrecta())
                else:
                    break        
            except:
                users = []
                        
        if event == 'Registrarse':
            window.hide()
            menu_signin.start()
            window.un_hide()

    return window    

