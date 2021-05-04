import PySimpleGUI as sg

def build_login():
    """ Construye la ventana del inicio de sesion del usuario"""


    layout =[[sg.T("Usuario"), sg.InputText(key='-USER-')],
            [sg.T("Contraseña"), sg.InputText(key='-PASS-')],
            [sg.Submit("LogIn") ],
            [sg.T("No estas registrado?")],
            [sg.Button('Registrarse')]]

    window = sg.Window('Inicio de sesion', layout)
    return window

def build_no_registrado():
        '''construye la ventana que avisa que no esta resgistrado el usuario'''
        layout = [[sg.Text('El usuario ingresado es incorrecto o no esta registrado, por favor registrese para continuar')],
                [sg.Ok()]]

        window = sg.Window('Aviso', layout)
        return window

def build_contra_incorrecta():
        '''contruye la ventana que avisa que la contraseña ingresada es incorrecta'''
        layout = [[sg.Text('La contraseña ingresada es incorrecta')],
                [sg.Ok()]]
        window = sg.Window('Aviso', layout)
        return window                        