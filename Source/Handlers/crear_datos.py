import csv, json, pandas
from posixpath import split

def crear(semana):
    ''' crea un archivo con los datos a usar y un string con el criterio usado
        para elegir los datos  
        esta funcion no tiene retorno, solo crea un archivo
    '''

    # abre los dos datasets
    with open('data/netflix_titles.csv', 'r', encoding='utf-8') as pal, open('data/appstore_games.csv', 'r', encoding='utf-8') as img:
        
        # criterios y datos a utilizar
        diccionario = {}
        criterios = definir_criterios(pal, img)

        # carga el diccionario con los datos divididos por dia y por franja horaria
        for i, dia in enumerate(semana):
            crit = criterios[i]

            diccionario[dia] = {
                'imagenes': {
                    'criterio': crit[0][1],
                    'data': list(crit[0][0]),
                },
                'palabras': {
                    'criterio': crit[1][1],
                    'data': list(crit[1][0]),
                }
            }

        # crea y guarda los datos en json
        with open('data/datos_juego.json', 'w', encoding='utf-8') as json_new:
            json.dump(diccionario, json_new, indent=4, ensure_ascii= False)

def definir_criterios(pal, img):
    ''' Los criterios para elegir los datos y una descripcion.   
        Se organiza como:   
          
        criterios(tupla) 
            --- dia(tupla) 
                --- imagenes o texto(tupla)
    '''
    dataframe_pal = pandas.read_csv(pal)
    dataframe_img = pandas.read_csv(img)

    return [
        (   # ----- lunes con imagenes -----
            (dataframe_img[dataframe_img['Original Release Date'] >= '1/1/2001']['Icon URL'][:20],
            'Juegos de la app store creados luego del año 2000'), 
            
            # ----- lunes con texto -----
            (dataframe_pal[(dataframe_pal['type'] == 'TV Show') & (dataframe_pal['duration'] > '2')]['title'][:20], 
            'Series de netflix con mas de 2 temporadas') 
        ), 
        (   # ----- martes con imagenes -----
            (dataframe_img[(dataframe_img['ID'].apply(str).str[-1:] == '1') & (dataframe_img['User Rating Count'] > 400)]['Icon URL'][:20], 
            'Juegos de la app store con mas de 400 reseñas y un id que termina en uno'),
            
            # ----- martes con texto -----
            (dataframe_pal[(dataframe_pal['type'] == 'Movie') & (dataframe_pal['duration'] > '60')]['title'][:20], 
            'Peliculas de netflix con mas de 60 minutos')
        ),
        (   # ----- miercoles con imagenes -----
            (dataframe_img[(dataframe_img['Languages'].str.split(',').str.len() > 5) & (dataframe_img['Current Version Release Date'] >= '1/1/2019')]['Icon URL'][:20], 
            'Los juegos de la app store con mas de 20 años de diferencia entre versiones'), 
            
            # ----- miercoles con texto -----
            (dataframe_pal[(dataframe_pal['type'] == 'TV Show') & ((1980 < dataframe_pal['release_year']) & (dataframe_pal['release_year'] > 2000))]['title'][:20], 
            'Peliculas de netflix creadas entre los años 1980 y 2000')
        ), 
        (   # ----- jueves con imagenes -----
            (dataframe_img[(dataframe_img['Price'] > 2) & (dataframe_img['Primary Genre'] == "Games")]['Icon URL'][:20],
            'Juegos con un precio mayor a 2'), 
            
            # ----- jueves con texto -----
            (dataframe_pal[(dataframe_pal['type'] == 'TV Show') & (['Dramas' in data for data in list(dataframe_pal['listed_in'])])]['title'][:20],
            'Series de netflix que aparecen en la categoria de dramas')
        ),
        (   # ----- viernes con imagenes -----
            (dataframe_img[(['FR' in data for data in list(dataframe_img['Languages'].apply(str))]) & (dataframe_img['Name'].str[0].str.lower() == 'r')]['Icon URL'][:20],
            'Juego de la app store con lenguaje frances que su nombre empieza con r'), 
            
            # ----- viernes con texto -----
            (dataframe_pal[['robot' in data for data in list(dataframe_pal['description'])]]['title'][:20]
            , 'Peliculas o series de netflix cuya descripcion contiene la palabra robot')
        )
    ]