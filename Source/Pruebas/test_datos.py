import unittest, json, os
from ..Handlers.elegir_datos import elegir_criterio
from ..Handlers.crear_datos import crear

path_datos = "data/datos_juego.json"

class test_elegir(unittest.TestCase):
    """ Serian pruebas para seleccion de criterios de juego """
    
    def test_json_no_existe(self):
        """ Prueba que la seleccion de criterios funcione 
            si no hay un json de datos para elegir """
        
        data = None
        try:
            with open(path_datos, "r") as file:
                data = json.load(file)
            os.remove(path_datos)
        
            self.assertTrue( 
                isinstance(elegir_criterio(), dict), 
                "el retorno de la funcion no es el esperado"
            )

            with open(path_datos, "w") as file:
                json.dump(data, file, indent = 4)
        except:
            crear(["lunes", "martes", "miercoles", "jueves", "viernes"])
            self.assertTrue( 
                isinstance(elegir_criterio("imagenes"), dict), 
                "el retorno de la funcion no es el esperado"
            )

    def test_json_existe(self):
        """ Prueba Prueba que la seleccion de criterios 
            funcione si el json de datos existe"""

        self.assertTrue( 
            isinstance(elegir_criterio("imagenes"), dict), 
            "el retorno de la funcion no es el esperado"
        )

class test_crear_datos(unittest.TestCase):
    """ Serian pruebas para la funcion que crea los criterios de juego """

    def test_funcionamiento(self):
        def existe_json():
            try:
                with open(path_datos, "r", encoding="utf8") as file:
                    json.load(file)

                return True
            except:
                return False
        
        os.remove(path_datos)
        crear(["lunes", "martes", "miercoles", "jueves", "viernes"])

        self.assertTrue(existe_json(), "el archivo no fue creado o no es un json")

    