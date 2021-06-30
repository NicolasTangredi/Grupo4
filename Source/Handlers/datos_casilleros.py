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

                # toma los bytes de imagen recibidos y los lee
                byte_img = req.content
                img = Image.open(io.BytesIO( byte_img ))

                # recorta el tamanio de la imagen y lo transforma a png ya
                # que PySimpleGUI no acepta jpgs
                with io.BytesIO() as f:
                    img.thumbnail((100, 102))
                    img.save(f, format='PNG')

                    # lo vuleve a transformar a bytes con las modificaciones
                    png = f.getvalue()
                    return png
        
        return elem

    # elige las palabras o imagenes a mostrar aleatoriamente
    filasDatos = []
    for _i in range( (x * y) // coincidencias ):
        index = random.randint(0, len(datos) - 1)
        
        elem = crearDato(datos[index])

        filasDatos.extend([elem] * coincidencias)
        
        del datos[index]

    # revuelv el arreglo y pense en retornar como una especie de matriz
    random.shuffle(filasDatos)
    return  ([filasDatos[i:i+x] for i in range(0, y*x, x)], crit)

def crearCasillasVacias(x, y, coinc):
    ''' retorna una especie de matriz con botones vacios'''

    col = []
    cant = ((x*y) // coinc) * coinc

    for i in range(y):
        row = []
        for j in range(x):
            if(cant > 0):
                row.append(sg.Button(key=f"CARD-{j},{i}", size=(12,6)))
                cant -= 1
            else:
                break
        col.append(row)
    return col
    