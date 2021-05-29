import csv, json
from posixpath import split

def crear(semana):
    ''' crea un archivo con los datos a usar y un string con el criterio usado
        para elegir los datos  
        esta funcion no tiene retorno, solo crea un archivo
    '''

    # abre los dos datasets
    with open('data/netflix_titles.csv', 'r', encoding='utf-8') as data, open('data/appstore_games.csv', 'r', encoding='utf-8') as data2:
        
        # criterios y datos a utilizar
        diccionario = {}
        full_data = (csv.DictReader(data2), csv.DictReader(data))
        criterios = definir_criterios()

        # carga el diccionario con los datos divididos por dia y por franja horaria
        for i, dia in enumerate(semana):
            crit = criterios[i]

            diccionario[dia] = {
                'imagenes': {
                    'criterio': crit[0][1],
                    'data': crit[0][0](full_data),
                },
                'palabras': {
                    'criterio': crit[1][1],
                    'data': crit[1][0](full_data),
                }
            }

            # reset de los lectores de archivos
            data.seek(0)
            data2.seek(0)

        # crea y guarda los datos en json
        with open('data/datos_juego.json', 'w', encoding='utf-8') as json_new:
            json.dump(diccionario, json_new, indent=4, ensure_ascii= False)

def definir_criterios():
    ''' Los criterios para elegir los datos y una descripcion.   
        Se organiza como:   
          
        criterios(tupla) 
            --- dia(tupla) 
                --- imagenes o texto(tupla)
    '''

    ""
    

    # en general, se filtra a los datos por un criterio definido y
    # se mapea el filterObject, quedandose con el dato que se necesite,
    # para despues castearlo el map a lista
    criterios = [
        (   # lunes con imagenes
            (lambda data: list(map( lambda item: item['Icon URL'], filter(lambda row: int(row['Original Release Date'].split('/')[2]) > 2000, data[0])))[:20]
            , 'Juegos de la app store creados luego del año 2000'), 
            
            # lunes con texto
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: row['type'] == 'TV Show' and int(row['duration'].split(' ')[0]) > 2, data[1])))[:20]
            , 'Series de netflix con mas de 2 temporadas'), 
        ), 
        (   # martes con imagenes
            (lambda data: list(map( lambda item: item['Icon URL'], filter(lambda row: row['ID'][-1] == '1' and int(0 if not row['User Rating Count'] else row['User Rating Count']) > 400, data[0])))[:20]
            , 'Juegos de la app store con mas de 400 reseñas y un id que termina en uno'),
            
            # martes con texto
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: row['type'] == 'Movie' and 'Horror Movies' in row['listed_in'] and int(row['duration'].split(' ')[0]) > 60, data[1])))[:20]
            , 'Peliculas de terror en netflix con mas de 60 minutos')
        ),
        (   # miercoles con imagenes
            (lambda data: list(map( lambda item: item['Icon URL'], filter(lambda row: len(row['Languages'].split(',')) > 5 and int(row['Current Version Release Date'].split('/')[-1]) > 2018, data[0])))[:20]
            , 'Los juegos de la app store con mas de 20 años de diferencia entre versiones'), 
            
            # miercoles con texto
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: row['type'] == 'TV Show' and 1980 < int(row['release_year']) > 2000, data[1])))[:20]
            , 'Peliculas de netflix creadas entre los años 1980 y 2000')
        ), 
        (   # jueves con imagenes
            (lambda data: list(map( lambda item: item['Icon URL'], filter(lambda row: float(0 if row['Price'] in ['Price', ''] else row['Price']) > 2 and 'Puzzle' in row['Genres'], data[0])))[:20]
            , 'Juegos del genero puzzle con un precio mayor a 2'), 
            
            # jueves con texto
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: row['type'] == 'TV Show' and 'Dramas' in row['listed_in'], data[1])))[:20]
            , 'Series de netflix que aparecen en la categoria de dramas')
        ),
        (   # viernes con imagenes
            (lambda data: list(map( lambda item: item['Icon URL'], filter(lambda row: 'FR' in row['Languages'] and row['Name'][0].lower() == 'r', data[0])))[:20]
            , 'Juego de la app store con lenguaje fances que su nombre empieza con r'), 
            
            # viernes con texto
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: 'robot' in row['description'].lower(), data[1])))[:20]
            , 'Peliculas o series de netflix cuya descripcion contiene la palabra robot')
        )
    ]

    return criterios