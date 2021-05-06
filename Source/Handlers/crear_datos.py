import csv, json

def crear(semana):
    ''' crea un archivo con los datos a usar y un string con el criterio usado
        para elegir los datos  
        esta funcion no tiene retorno, solo crea un archivo
    '''
    

    # abre los dos datasets
    with open('data/netflix_titles.csv', 'r', encoding='utf-8') as data, open('data/summer.csv', 'r', encoding='utf-8') as data2:
        
        # criterios y datos a utilizar
        diccionario = {}
        full_data = (csv.DictReader(data2), csv.DictReader(data))
        criterios = definir_criterios()

        # carga el diccionario con los datos divididos por dia y por franja horaria
        for i, dia in enumerate(semana):
            crit = criterios[i]

            diccionario[dia] = {
                'maniana': {
                    'criterio': crit[0][1],
                    'data': crit[0][0](full_data),
                },
                'tarde': {
                    'criterio': crit[1][1],
                    'data': crit[1][0](full_data),
                }
            }

            # reset de los lectores de archivos
            data.seek(0)
            data2.seek(0)

        # crea y guarda los datos en json
        with open('data/datos_juego.json', 'w', encoding='utf-8') as json_new:
            json.dump(diccionario, json_new, indent=4)

def definir_criterios():
    ''' Los criterios para elegir los datos y una descripcion.   
        Se organiza como:   
          
        criterios(set) 
            --- dia(set) 
                --- mañana y tarde(tupla)
    '''

    # en general, se filtra a los datos por un criterio definido y
    # se mapea el filterObject, quedandose con el dato que se necesite,
    # para despues castearlo el map a lista
    criterios = [
        (
            (lambda data: list(map( lambda item: item['Athlete'], filter(lambda row: row['Discipline'] == 'Swimming' and row['Medal'] == 'Gold', data[0])))[:20]
            , 'Atletas olimpicos de la disciplina de natacion con medallas de oro'), 
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: row['type'] == 'TV Show' and int(row['duration'].split(' ')[0]) > 2, data[1])))[:20]
            , 'Series de netflix con mas de 2 temporadas'), 
        ),
        (
            (lambda data: list(map( lambda item: item['Athlete'], filter(lambda row: row['Discipline'] == 'Fencing' and row['Medal'] == 'Silver', data[0])))[:20]
            , 'Atletas olimpicos de la disciplina de esgrima con medallas de plata'),
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: row['type'] == 'Movie' and 'Dramas' in row['listed_in'] and int(row['duration'].split(' ')[0]) > 60, data[1])))[:20]
            , 'Peliculas de terror en netflix con mas de 60 minutos')
        ),

        (   
            (lambda data: list(map( lambda item: item['Athlete'], filter(lambda row: row['Year'] == '2008' and row['Gender'] == 'Women', data[0])))[:20]
            , 'Atletas olimpicos que participaron en las olimpiadas del 2008 y son mujeres'), 
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: row['type'] == 'TV Show' and 1980 < int(row['release_year']) > 2000, data[1])))[:20]
            , 'Peliculas de netflix creadas entre los años 1980 y 2000')
        ),

        (   
            (lambda data: list(map( lambda item: item['Athlete'], filter(lambda row: row['City'] == 'Athens' and row['Sport'] == 'Gymnastics', data[0])))[:20]
            , 'Gimnastas olimpicos que participaron en las olimpiadas en Atenas'), 
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: row['type'] == 'TV Show' and 'Dramas' in row['listed_in'], data[1])))[:20]
            , 'Series de netflix que aparecen en la categoria "Dramas"')
        ),

        (   
            (lambda data: list(map( lambda item: item['Athlete'], filter(lambda row: row['Country'] == 'USA' and row['Athlete'][0].lower() in 'cl', data[0])))[:20]
            , 'Atletas olimpicos de Eestados Unidos cuyo apellido comienza con una c o una l '), 
            (lambda data: list(map( lambda item: item['title'], filter(lambda row: 'robot' in row['description'].lower(), data[1])))[:20]
            , 'Peliculas o series de netflix cuya descripcion contiene la palabra robot')
        )
    ]

    return criterios