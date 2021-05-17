import json

def set_config(key, valor, usuario):
    """recibe la key del diccionario configuracion, un valor y el nombre del usuario.
        Busca al usuario y guarda el valor en la configuracion del usuario."""
    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["nombre"] == usuario:
                user["configuracion"][key] = valor
                break
    with open("data/usuarios.json", "w", encoding="utf8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)          


def set_casillas(dimension, usuario):
    """recibe las dimensiones del tablero y las guarda en su configuracion"""
    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["nombre"] == usuario:
                user["configuracion"]["cant_casillas"] = dimension
                break
    with open("data/usuarios.json", "w", encoding="utf8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)          

def set_elemento(elemento, usuario):
    """recibe el elemtento que estara en el tablero y las guarda en su configuracion"""
    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["nombre"] == usuario:
                user["configuracion"]["tipo_elemento"] = elemento
                break
    with open("data/usuarios.json", "w", encoding="utf8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)        

def set_tiempo(tiempo, usuario):
    """recibe la duracion de la partida y la guarda en su configuracion"""
    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["nombre"] == usuario:
                user["configuracion"]["tiempo"] = tiempo
                break
    with open("data/usuarios.json", "w", encoding="utf8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)          

def set_color(color, usuario):
    """recibe las dimensiones del tablero y las guarda en su configuracion"""
    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["nombre"] == usuario:
                user["configuracion"]["paleta_de_colores"] = color
                break
    with open("data/usuarios.json", "w", encoding="utf8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)          