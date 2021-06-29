import json

def crear_usuario(nombre, contra, genero, edad):
    '''crea un usuario'''
    usuario = {"nombre": nombre,
              "contraseña": contra,
              "edad": edad,
              "genero": genero,
              "estadisticas": { 'partidas_ganadas': 0,
                                'partidas_perdidas': 0,
                                "puntaje_maximo": [["facil" ,0],["dificil" ,0],["dificil" ,0]],
                                },
              'configuracion': {'cant_casillas': "4x4",
                                'tipo_elemento': 'palabras',
                                'cant_coincidencias': 2,
                                'tiempo': 120,
                                'paleta_de_colores': 'DarkTeal5'},
              "historial" : [],
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
              
def usuario_disponible(usuario):
    """ recibe un nombre de usuario y devuelve True si el nombre no 
        no pertenece a otro usuario registrado y False si ya esta en uso"""
    if usuario not in usuarios_registrados():
        return True
    else:
        return False    


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


def validacion_signin(user,age,genre):
    """Recibe los datos ingresados durante el registro de usuario.
        y devuelve un nro. si los datos son validos devuelve 0, si 
        el username no es valido devuelve 1, si la edad no es valida
        devuelve 2 y si el genero no es valido devuelve 3"""
    if len(user) == 0 or user[0] == ' ' or  not usuario_disponible(user) :
        return 1
    elif len(age) == 0 or age[0] == ' ':
        return 2
    elif len(genre) == 0 or genre[0] == ' ':
        return 3       
    else:
        try:
            i = 0
            print(int(age))
            i=+ 1
            print(int(genre))
            return 3
        except ValueError:
            if i == 0:
                return 2
            else:
                return 0  
            

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
    """devuelve un diccionario con los nombres como llave y el puntaje maximo como valor"""
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
                usuar = user["nombre"]
                break
    return usuar
            
    
                
def usuario_conectado_profile():
    """devuelve el usuario conectado"""

    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["conectado"] == 1:
                usuar = user
                break
    return usuar        
            



def dame_puntuaciones_pa():
    """me devuelve un diccionario con los 10 usuarios con mayor puntuacion como llaves y claves"""
    puntajes = puntajes_usuarios()
    points = dict(sorted(puntajes.items(),key=lambda x: x[1] ,reverse=True)[:10])
    return points
  
                
    

def get_time ():
    """retorna el tiempo de juego definido por el usuario"""
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            for buscar_usuario in datos:
                if usuario_conectado() == buscar_usuario["nombre"]:
                    tiempo = buscar_usuario["configuracion"]["tiempo"]
                    break
    return tiempo  

def datos_partida(usuario,puntaje_logrado,tiempo_jugado):
    """
    recibe datos de la partida y retorna un diccionario con 
    el nombre de usuario y los datos de la partida jugada cargados"""

    config = usuario["configuracion"]
    niveles = ["facil", "medio", "dificil"]
    return {
        "nombre": usuario["nombre"],
        "puntaje": puntaje_logrado,
        "tiempo": config["tiempo"] - tiempo_jugado,
        "dificultad": niveles[(config["tiempo"] - 30) % 30]
    }
    
def desconectar_todos():
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
        datos = json.load(usuario)
        for buscar_usuario in datos:
            if buscar_usuario["conectado"] ==1:
                buscar_usuario["conectado"] = 0
        with open("data/usuarios.json","w", encoding="utf8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
            
def genero():
    """retorna una lista con todos los generos registrados"""
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            gender = []
            for buscar_usuario in datos:
                if buscar_usuario["genero"] not in gender:
                    gender.append(buscar_usuario["genero"])                   
    return gender 
    








                        
                        










