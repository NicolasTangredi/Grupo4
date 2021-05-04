import PySimpleGUI as sg
from Source.Ventanas import ventana_signin
from Source.Handlers import usuario

def start():
    """Ejecuta la ventana del menu de registro de usuario"""

    window = loop()
    window.close()


def loop():

    window = ventana_signin.build_signin()
    while True:
        event, values = window.read()

        if event == None or event == "Cancel":
            break

        if event == "SignIn":
            user = values["-USER-"]
            pwd = values["-PASS-"]
            age = values["-AGE-"]
            genre = values["-GENRE-"]
            new_user = usuario.crear_usuario(user,pwd,age,genre)
            usuario.añadir_usuario(new_user)
            break
    return window        


