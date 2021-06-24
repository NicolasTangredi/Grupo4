import json
from ..Handlers import usuario as uuser

def calcular_puntos (boolean,cant_punt,difficult="facil bro"):
    """resta o suma segun si se equivoco o no en las coincidencias y segun la dificultad elegida"""
    if boolean:
        cant_punt = sumar_puntos(boolean,cant_punt,difficult)
    else:
        cant_punt = restar_puntos(boolean,cant_punt,difficult)
    return cant_punt    
    

def sumar_puntos (boolean,es_igual,difficult="facil bro"):
    """si las cartas fueron iguales entonces suma puntos a la funcion"""
    if boolean and difficult == "facil bro":
        es_igual = es_igual + 3
    elif boolean and difficult == "madio pa":
        es_igual = es_igual + 6
    else:
        if boolean and difficult == "re dificil hermano":
            es_igual = es_igual + 9
    return es_igual

def restar_puntos (boolean,es_igual,difficult="facil bro"):
    """si se equivoco una cierta cantidad de veces entonces resta puntos"""
    if boolean and difficult == "facil bro":
        es_igual = es_igual - 3
    elif boolean and difficult == "madio pa":
        es_igual = es_igual - 8
    else:
        if boolean and difficult == "re dificil hermano":
            es_igual = es_igual - 12
    return es_igual

def sos_pro (max_punt,puntaje_logrado,nombre,dificultad):
    """cambia el puntaje del usuario en caso de que la puntuacion lograda haya sido mayor que su 
    puntuacion maxima,la puntuacion lograda se determina a traves de la funcion 'fin_juego'"""
    cambiado = False
    if max_punt < puntaje_logrado:
        with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            for buscar_usuario in datos:
                if nombre == buscar_usuario["nombre"]:
                    buscar_usuario["estadisticas"]["puntaje_maximo"] = puntaje_logrado
                    buscar_usuario["estadisticas"]["dif_puntMax"] = dificultad
                    break
            with open("data/usuarios.json","w", encoding="utf8") as file:
                json.dump(datos, file, indent=4, ensure_ascii=False)
            cambiado = True
    return cambiado

def pro_o_manco (var,nombre):
    """recibe un boolean y suma +1 en las partidas ganadas o perdidas del jugador"""
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
        datos = json.load(usuario)
        for buscar_usuario in datos:
            if nombre == buscar_usuario["nombre"]:
                if var:
                    buscar_usuario["estadisticas"]["partidas_ganadas"] = buscar_usuario["estadisticas"]["partidas_ganadas"] + 1
                else:
                    buscar_usuario["estadisticas"]["partidas_perdidas"] = buscar_usuario["estadisticas"]["partidas_perdidas"] + 1                         
                break
    with open("data/usuarios.json","w", encoding="utf8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)

def update_accumulated_points(user,cant_points):
    """aumenta la cantidad de puntos acumulados"""
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            for buscar_usuario in datos:
                if user["nombre"] == buscar_usuario["nombre"]:
                    buscar_usuario["in_game"]["cant_puntos"] = buscar_usuario["in_game"]["cant_puntos"] + cant_points
                    break
            with open("data/usuarios.json","w", encoding="utf8") as file:
                json.dump(datos, file, indent=4, ensure_ascii=False)

def puntuacion_acumulada():
    """retorna la cantidad de puntos acumulados hasta el momento"""
    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["conectado"] == 1:
                usuar = user["in_game"]["cant_puntos"]
                break
    return usuar       
                
def clear_accumulated_points(user):
    """pone en 0 la cantidad de puntos del usuario"""
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            for buscar_usuario in datos:
                if user["nombre"] == buscar_usuario["nombre"]:
                    buscar_usuario["in_game"]["cant_puntos"] = 0
                    break
            with open("data/usuarios.json","w", encoding="utf8") as file:
                json.dump(datos, file, indent=4, ensure_ascii=False)
                
def fin_juego (total_aciertos,punt_total,tiempo_sobrante,user):
    """calcula la puntuacion total del usuario y actualiza el historial del usuario"""
    history_channel = uuser.datos_partida(user,punt_total,tiempo_sobrante)
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            for buscar_usuario in datos:
                if user["nombre"] == buscar_usuario["nombre"]:
                    buscar_usuario["historial"].append(history_channel)
                    break
            with open("data/usuarios.json","w", encoding="utf8") as file:
                json.dump(datos, file, indent=4, ensure_ascii=False)
    tot = total_aciertos * punt_total + tiempo_sobrante
    return tot

def div(dificultad,puntajes,dato):
    """recibe un diccionario con nombre-dificultad y puntajes-dificultad para crear una lista solo con la dificultad
    recibida en dato"""
    x = list(puntajes.keys())
    lista = []
    for user in x:
        if dificultad[user] == dato:
            lista.append([user,puntajes[user],dato])      
    return lista

def dividir_puntajes(dif):
    """crea un diccionario de listas ordenadas por puntuacion mas alta segun la dificultad que reciba"""
    puntajes = uuser.dame_puntuaciones_pa()
    dificultad = uuser.dif_usuarios()
    if dif == "facil":
        f = div(dificultad,puntajes,"facil")
        xd = sorted(f,key=lambda x: x[1] ,reverse=True)[:5]
    elif dif == "medio":
        f = div(dificultad,puntajes,"medio")
        xd = sorted(f,key=lambda x: x[1] ,reverse=True)[:5]
    elif dif == "dificil":
        f = div(dificultad,puntajes,"dificil")
        xd = sorted(f,key=lambda x: x[1] ,reverse=True)[:5]         
    return xd