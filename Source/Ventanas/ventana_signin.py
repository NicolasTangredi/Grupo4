import PySimpleGUI as sg

def build_signin():
     """ Construye la ventana del registro del usuario"""


     layout = [[sg.T("Usuario"), sg.InputText(key='-USER-')],
                [sg.T("Contraseña"), sg.InputText(key='-PASS-')],
                [sg.T("Edad"), sg.InputText(key='-AGE-')],
                [sg.T("Genero"), sg.InputText(key='-GENRE-')],
                [sg.Submit("SignIn"), sg.Cancel()]]

     window = sg.Window('Registrarse', layout) 
     return window         