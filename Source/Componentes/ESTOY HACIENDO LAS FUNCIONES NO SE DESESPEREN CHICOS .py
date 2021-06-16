import json
def fin_juego (total_aciertos,punt_total,tiempo_sobrante,user):
    """calcula la puntuacion total del usuario y actualiza el historial del usuario"""
    history_channel = datos_partida(user,punt_total,tiempo_sobrante)
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

def calcular_puntos (boolean,cant_punt,difficult="facil bro",n_intento=0):
    """resta o suma segun si se equivoco o no en las coincidencias y segun la dificultad elegida"""
    if boolean:
        cant_punt = sumar_puntos(boolean,cant_punt,difficult)
    else:
        #Es necesario incrementar "n_intento" desde fuera de la funcion y resetearlo cada 3 intento
        if n_intento = 3:
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

def que_dificultad_papa (cant_coincidencias,time):
    """ define la dificultad en el rango (1-3) segun la cantidad de coincidencias y tiempo del usuario"""
    if (cant_coincidencias == 1 or cant_coincidencias == 2 or cant_coincidencias == 3)  and time == 120:
        jg_diff = "facil bro"
    elif (cant_coincidencias == 2 or cant_coincidencias == 1 or cant_coincidencias == 3) and time == 90:
        jg_diff = "madio pa"
    else:
        jg_diff = "re dificil hermano"     
    return jg_diff    

def sos_pro (max_punt,puntaje_logrado,nombre):
    """cambia el puntaje del usuario en caso de que la puntuacion lograda haya sido mayor que su 
    puntuacion maxima,la puntuacion lograda se determina a traves de la funcion 'fin_juego'"""
    cambiado = False
    if max_punt < puntaje_logrado:
        with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            for buscar_usuario in datos:
                if nombre == buscar_usuario["nombre"]:
                    buscar_usuario["estadisticas"]["puntaje_maximo"] = puntaje_logrado
                    break
            with open("data/usuarios.json","w", encoding="utf8") as file:
                json.dump(datos, file, indent=4, ensure_ascii=False)
            cambiado = True
    return cambiado                 

def datos_partida(usuario,puntaje_logrado,tiempo_jugado):
    """
    recibe un diccionario con 4 llaves y retorna un diccionario con 
    el nombre de usuario y los datos de la partida jugada cargados"""
    dic={}
    dic["nombre"]=usuario["nombre"]
    dic["puntaje"]=puntaje_logrado
    dic["tiempo"]=usuario["configuraciones"]["tiempo"] - tiempo_jugado
    dic["dificultad"]=que_dificultad_papa(usuario["estadisticas"]["cant_coincidencias"],usuario["estadisticas"]["tiempo"])
    
    return dic

     
