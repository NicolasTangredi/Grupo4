import PySimpleGUI as sg

def build_signin():
     """ Construye la ventana del registro del usuario"""


     layout = [[sg.T("Usuario", size=(10, 1)), sg.InputText(key='-USER-')],
                [sg.T("Contraseña", size=(10, 1)), sg.InputText(key='-PASS-')],
                [sg.T("Edad", size=(10, 1)), sg.InputText(key='-AGE-')],
                [sg.T("Genero", size=(10, 1)), sg.InputText(key='-GENRE-')],
                [sg.Submit("SignIn", size=(15, 1)), sg.Cancel(size=(15, 1))]]

     window = sg.Window('Registrarse', layout, element_justification='center') 
     return window         