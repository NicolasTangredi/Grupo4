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
