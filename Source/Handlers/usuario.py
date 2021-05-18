import json

def crear_usuario(nombre, contra, genero, edad):
    '''crea un usuario'''
    usuario = {"nombre": nombre,
              "contraseña": contra,
              "edad": edad,
              "genero": genero,
              "estadisticas": { 'partidas_ganadas': 0,
                                'partidas_perdidas': 0,
                                'puntaje_maximo': 0},
              'configuracion': {'cant_casillas': 0,
                                'tipo_elemento': 'texto',
                                'cant_coincidencias': 0,
                                'tiempo': 120,
                                'paleta_de_colores': 'color'},
              #Si el usuario esta desconectado = 0/Si el usuario esta conectado = 1
              'conectado': 0
               }                                   
    return usuario

def añadir_usuario(user):
    '''añade un usuario al archivo usuarios.json'''
    try:
        with open("data/usuarios.json", "r", encoding="utf8") as file:
            lista_de_usuarios = json.load(file)
    except FileNotFoundError:
        lista_de_usuarios = []

        
    lista_de_usuarios.append(user)
    with open("data/usuarios.json", "w", encoding="utf8") as file:
        json.dump(lista_de_usuarios, file, indent=4, ensure_ascii=False)   
              


def usuarios_registrados():
    '''devuelve una lista con los nombres de los usuarios registrados'''
    with open('data/usuarios.json',  encoding ='utf8') as usuarios:
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


# arreglado brother B)

def user_logged(nom):
    """conecta al usuario del que se ingrso nombre y contraseña en sus argumentos""" 
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
        datos = json.load(usuario)
        for buscar_usuario in datos:
            if nom == buscar_usuario["nombre"]:
                buscar_usuario["conectado"] = 1
                break
        with open("data/usuarios.json","w", encoding="utf8") as file:
           json.dump(datos, file, indent=4, ensure_ascii=False)
                         

def user_disconnected(nom):
    """devuelve una lista con el nombre y contraseña del usuario logeado""" 
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
        datos = json.load(usuario)
        for buscar_usuario in datos:
            if nom == buscar_usuario["nombre"]:
                buscar_usuario["conectado"] = 0
                break
        with open("data/usuarios.json","w", encoding="utf8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
            
def puntajes_usuarios():
    """devuelve un diccionario con los nombres como llave y el puntaje como valor"""
    with open('data/usuarios.json', encoding="utf8") as usuario:
        datos = json.load(usuario)

        dic = {}
        for users in datos:
            dic[users["nombre"]]= users["estadisticas"]["puntaje_maximo"]
        return dic 
  
def stats_logged():
    """devuelve las estadisticas del usuario conectado"""
    
    with open('data/usuarios.json',"r", encoding="utf8") as usuar:
        usuar = json.load(usuar)

        for usuario in usuar:
            if usuario["conectado"] == 1:
                num1 = usuario["estadisticas"]["partidas_ganadas"]
                num2 = usuario["estadisticas"]["partidas_perdidas"]
                num3 = usuario["estadisticas"]["puntaje_maximo"]
        
        return num1,num2,num3
def usuario_conectado():
    """devuelve el nombre del usuario conectado"""

    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["conectado"] == 1:
                return user["nombre"]


def max_punt():
    """retorna una lista con los nombres(impares) y puntajes(pares) de los 3 mejores jugadores"""
    lista = []
    puntajes = puntajes_usuarios()
    k=1
    for i in range(3):
        max=-100
        for jugador in puntajes.keys():
            if puntajes[jugador] > max:
                puntos_max=puntajes[jugador]
                jugador_max=jugador
        lista.append(jugador_max)
        lista.append(puntos_max)        
        puntajes.pop(jugador_max)
        k=k+2
    return lista



                        
                        










