import json

def crear_usuario(nombre, contra, genero, edad):
    '''crea un usuario'''
    usuario = {"nombre": nombre,
              "contraseña": contra,
              "edad": edad,
              "genero": genero}
    return usuario

def añadir_usuario(user):
    '''añade un usuario al archivo usuarios.json'''
    with open("'data/usuarios.json'", "w", encoding="utf8") as file:
        lista_de_usuarios = json.load(file)
        lista_de_usuarios.append(user)
        json.dump(lista_de_usuarios, file, indent=4, ensure_ascii=False)   
              


def usuarios_registrados():
    '''devuelve una lista con los nombres de los usuarios registrados'''
    with open('data/usuarios.json', encoding ='utf8') as usuarios:
        data_usuarios = json.load(usuarios)
        users = list(map(lambda x: x['nombre'], data_usuarios))
        return users

def check_contra (nombre,contra):
    with open('data/usuarios.json', encoding ='utf8') as file:
        users = json.load(file)
        for user in users:
            if user['nombre'] == nombre and user['contraseña'] == contra:
                return True
        return False        
                




