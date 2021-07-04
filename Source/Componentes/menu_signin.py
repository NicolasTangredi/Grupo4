import PySimpleGUI as sg
from Source.Ventanas import signin
from Source.Handlers import usuario

def start():
    """Ejecuta la ventana del menu de registro de usuario"""

    window = loop()
    window.close()


def loop():

    window = signin.build_signin()
    while True:
        event, values = window.read()

        if event == None or event == "Cancel":
            break

        if event == "SignIn":
            user = values["-USER-"]
            pwd = values["-PASS-"]
            age = values["-AGE-"]
            genre = values["-GENRE-"]
            i = usuario.validacion_signin(user,age,genre)
            if i == 1:
                sg.popup('el nombre de usuario no es valido o no esta disponible')
            elif i == 2:
                sg.popup("la edad ingresada no es valida, por favor ingrese un numero. Tenes que ser mayor de 5 años y menor de 120")
            elif i == 3:
                sg.popup('el genero ingresado no es valido, por favor ingrese caracteres validos')
            else:
                new_user = usuario.crear_usuario(user,pwd,genre,age)
                usuario.añadir_usuario(new_user)
                break    
    return window        


