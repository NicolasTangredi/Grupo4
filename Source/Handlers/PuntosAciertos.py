import json
from ..Handlers import usuario as uuser

def calcular_puntos (boolean,cant_punt,difficult):
    """resta o suma segun si se equivoco o no en las coincidencias y segun la dificultad elegida"""
    if boolean:
        x = sumar_puntos(cant_punt,difficult)
    else:
        x = restar_puntos(cant_punt,difficult)
    return x    
    

def sumar_puntos (es_igual,difficult):
    """si las cartas fueron iguales entonces suma puntos a la funcion"""
    if difficult == "facil":
        es_igual = es_igual + 3
    elif difficult == "madio":
        es_igual = es_igual + 6
    elif difficult == "dificil":
        es_igual = es_igual + 9
    return es_igual

def restar_puntos (es_igual,difficult):
    """si se equivoco una cierta cantidad de veces entonces resta puntos"""
    if difficult == "facil":
        es_igual = es_igual - 1
    elif difficult == "madio":
        es_igual = es_igual - 2
    elif difficult == "dificil":
        es_igual = es_igual - 3
    return es_igual

def points_max(user,dificultad):
    if dificultad == "facil":
        max_punt = user["estadisticas"]["puntaje_maximo"][0][1]
    elif dificultad == "medio":
        max_punt = user["estadisticas"]["puntaje_maximo"][1][1]   
    elif dificultad == "dificil":
        max_punt = user["estadisticas"]["puntaje_maximo"][2][1]
    return max_punt        

def sos_pro (max_punt,puntaje_logrado,nombre,dificultad):
    """cambia el puntaje del usuario en caso de que la puntuacion lograda haya sido mayor que su 
    puntuacion maxima,la puntuacion lograda se determina a traves de la funcion 'fin_juego'"""
    cambiado = False    
    if max_punt < puntaje_logrado:
        with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            for buscar_usuario in datos:
                if nombre == buscar_usuario["nombre"]:
                    if dificultad == "facil":
                        buscar_usuario["estadisticas"]["puntaje_maximo"][0][1] = puntaje_logrado
                    elif dificultad == "medio":    
                        buscar_usuario["estadisticas"]["puntaje_maximo"][1][1] = puntaje_logrado
                    elif dificultad == "dificil":
                        buscar_usuario["estadisticas"]["puntaje_maximo"][2][1] = puntaje_logrado    
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

def points_difficult(dificultad):
    with open('data/usuarios.json',"r+", encoding="utf8") as usuario:
        datos = json.load(usuario)
        lis = []
        for users in datos:
            if dificultad == "facil":
                lis.append([users["nombre"],users["estadisticas"]["puntaje_maximo"][0][1]])
            elif dificultad == "medio":
                lis.append([users["nombre"],users["estadisticas"]["puntaje_maximo"][1][1]])
            elif dificultad == "dificil":
                lis.append([users["nombre"],users["estadisticas"]["puntaje_maximo"][2][1]])      
    return lis  

def div(dificultad,puntajes,dato):
    """recibe un diccionario con nombre-dificultad y puntajes-dificultad para crear una lista solo con la dificultad
    recibida en dato"""
    x = list(puntajes.keys())
    lista = []
    for user in x:
        if dificultad[user] == dato:
            lista.append([user, puntajes[user]])      
    return lista

def dividir_puntajes(dif):
    """crea un diccionario de listas ordenadas por puntuacion mas alta segun la dificultad que reciba"""
    if dif == "facil":
        f = points_difficult("facil")
        xd = sorted(f,key=lambda x: x[1] ,reverse=True)[:5]
    elif dif == "medio":
        f = points_difficult("medio")
        xd = sorted(f,key=lambda x: x[1] ,reverse=True)[:5]
    elif dif == "dificil":
        f = points_difficult("dificil")
        xd = sorted(f,key=lambda x: x[1] ,reverse=True)[:5]         
    return xd