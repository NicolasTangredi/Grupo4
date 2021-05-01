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

    # intenta cargar los datos desde el archivo json, sino crea el
    # archivo y carga el archivo, si esto tambien falla imprime un
    # mensaje de error
    try:
        with open('data/json_new.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except:
        try:
            print('JSON no existe, creando uno nuevo')
            crear_datos.crear(semana)
            with open('data/json_new.json', 'r', encoding='utf-8') as json_file:
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

        if horario == 0:
            print(dia, ' por la maniana')
            return data[dia]['maniana']
        else:
            print(dia, ' por la tarde')
            return data[dia]['tarde']