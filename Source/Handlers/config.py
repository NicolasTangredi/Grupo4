import json

def set_config(values, usuario):
    """recibe la key del diccionario configuracion, un valor y el nombre del usuario.
        Busca al usuario y guarda el valor en la configuracion del usuario."""

    with open('data/usuarios.json',"r", encoding="utf8") as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user["nombre"] == usuario:
                    print (user["configuracion"])
                    user["configuracion"]= values
                    break
    with open("data/usuarios.json", "w", encoding="utf8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)          


