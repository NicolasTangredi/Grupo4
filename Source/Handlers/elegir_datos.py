import json, datetime, random
from ..Handlers import crear_datos

def elegir_criterio():
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
        # obtiene el dia y la hora
        dia = datetime.datetime.now().weekday()
        horario = datetime.datetime.now().hour

        # semana actual y si es mañana o tarde
        # los fines de semana es una criterio aleatorio
        try:
            dia = semana[dia]
        except:
            dia = semana[random.randint(0,4)]
        horario = horario // 12

        # elije los datos por dia y franja horaria
        if horario == 0:
            print(dia, ' por la mañana')
            return data[dia]['mañana']
        else:
            print(dia, ' por la tarde')
            return data[dia]['tarde']