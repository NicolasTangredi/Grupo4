import PySimpleGUI as sg

def build_login():
    """ Construye la ventana del inicio de sesion del usuario"""


    layout =[[sg.T("Usuario", size=(8,1)), sg.InputText(key='-USER-')],
            [sg.T("Contraseña", size=(8,1)), sg.InputText(key='-PASS-')],
            [sg.Submit("LogIn", size=(15,1), pad=(0,15))],
            [sg.T("No estas registrado?")],
            [sg.Button('Registrarse', size=(15,1))]]

    window = sg.Window('Inicio de sesion', layout, element_justification='center')
    return window
