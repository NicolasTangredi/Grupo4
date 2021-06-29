import json, datetime, random
from ..Handlers import crear_datos

def elegir_criterio( tipo_dato ):
    ''' devuelve un diccionario que contiene una lista de strings, con un criterio que
        cambia dependiendo del dia de la semana, y un string con una 
        descripcion del criterio usado.

        estructura:   
            {
                "criterio": string,
                "data": [string, string, ...] hasta 20 strings
            }
    '''
    
    semana = ['lunes','martes','miercoles','jueves','viernes']
    data = None   

    # intenta cargar los datos desde el archivo json
    try:
        with open('data/datos_juego.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except:

        # sino intenta crear el archivo y carga los datos
        try:
            print('JSON no existe, creando uno nuevo')
            crear_datos.crear(semana)
            with open('data/datos_juego.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        except:
            print('Parece que hay problemas con los datos')

    if data != None:
        # obtiene el dia y hora actual
        dia = datetime.datetime.now().weekday()
        hora = datetime.datetime.now().hour
        # los fines de semana es una criterio aleatorio
        try:
            dia = semana[dia]
        except:
            dia = semana[random.randint(0,4)]

        data_act = data[dia][tipo_dato]

        # devuelve los datos segun el horario
        if((hora // 12) == 1):
            print(f"hoy es {dia} por la tarde, estas jugando con: {tipo_dato}")
            return {
                "criterio": data_act["criterio"], 
                "data": data_act["data"][:20]
            }
        else:
            print(f"hoy es {dia} por la maniana, estas jugando con: {tipo_dato}")
            return {
                "criterio": data_act["criterio"], 
                "data": data_act["data"][20:40]
            }