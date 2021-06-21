import json

def puntajes_usuarios():
    """devuelve un diccionario con los nombres como llave y el puntaje maximo como valor"""
    with open('data/usuarios.json',encoding="utf8") as usuario:
        datos = json.load(usuario)
        dic = {}
        for users in datos:
            dic[users["nombre"]]= users["estadisticas"]["puntaje_maximo"]
        return dic

def dame_puntuaciones_pa():
    puntajes = puntajes_usuarios()
    points = dict(sorted(puntajes.items(),key=lambda x: x[1],reverse=True)[:10])
    return points

def dif_usuarios():
    """devuelve un diccionario con los nombres como llave y la difficultad como valor"""
    with open('data/usuarios.json', encoding="utf8") as usuario:
        datos = json.load(usuario)
        dic = {}
        for users in datos:
            dic[users["nombre"]]= users["estadisticas"]["dif_puntMax"]
        return dic
    
llaves = list(dame_puntuaciones_pa().keys())

print(dif_usuarios()[llaves[5]])