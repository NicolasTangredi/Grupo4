from multiprocessing import Value
import requests, io, random, PySimpleGUI as sg
from PIL import Image
from Source.Handlers.elegir_datos import elegir_criterio

def crearDatosJugada( tipo_elem, coincidencias, x, y ):
    ''' retorna una matriz de elementos, que serian las imagenes o
        palabras para las casillas
    '''

    data = elegir_criterio(tipo_elem)
    datos = data['data']
    crit = data['criterio']

    def crearDato(elem):
        if tipo_elem == "imagenes":
            # pide la imagen
            req = requests.get(elem)
            if ( req.ok ):

                # toma los bytes de imagen recibidos y los lee con
                # un lector BytesIO
                byte_img = req.content
                img = Image.open(io.BytesIO( byte_img ))

                # recorta el tamanio de la imagen y lo transforma a png ya
                # que PySimpleGUI no acepta jpgs
                with io.BytesIO() as f:
                    img.thumbnail((100, 100))
                    img.save(f, format='PNG')

                    # lo vuleve a transformar a bytes con las modificaciones
                    png = f.getvalue()
                    return png
        
        return elem

    # elige las palabras o imagenes a mostrar aleatoriamente
    filasDatos = []
    for _i in range( (x * y) // coincidencias ):
        index = random.randint(0, len(datos) - 1)
        
        filasDatos.extend([crearDato(datos[index]) for _i in range(coincidencias)])
        datos.pop(index)

    random.shuffle(filasDatos)
    return  ([filasDatos[i::x] for i in range(x)], crit)

def crearCasillasVacias(x, y):
    ''' retorna una matriz de botones vacios'''

    # doble list comprehension
    col = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(sg.Button(key=f"CARD-{j},{i}", size=(12, 6)))
        col.append(row)
    return col
    