from time import sleep

class Jugada():
    ''' es el controlador de la jugada, lleva la cuenta de los 
        elementos clickeados y si son iguales.
        para agregar un elemento se hace obj.update( boton, dato del boton )
        para reiniciar los elementos se hace obj.limpiar( tipo de dato )
    '''

    def __init__(self, tipo, coincidencias, maxAc):
        self.tipo = tipo
        self.aciertos = 0
        self.maxAc = maxAc
        self.elems = []
        self.botones = []
        self.max = coincidencias

    def update(self, boton, dato):
        ''' recibe el boton que fue clickeado y sus datos para
            chequear que sean iguales y si tiene todas las coincidencias
        '''

        self.elems.append(dato)
        self.botones.append(boton)

        # si el primer elemento aparece en todo el arreglo
        esIgual = self.elems.count(self.elems[0]) == len(self.elems)

        # si se equivoco o llego al max de coincidencias
        if( not esIgual):
            self.mala()
        elif ( len(self.elems) == self.max):
            self.buena()

    def mala(self):
        ''' pone los casilleros en blanco y reinicia los elementos y botones guardados
        '''
        
        # espera un rato y luego pone los botones en blanco
        sleep(0.5)
        for boton in self.botones:
            if(self.tipo == 'imagenes'):
                boton.Update(image_data="", image_size=(100,102), disabled=False)
            else:
                boton.Update("", disabled=False)

        self.elems.clear()
        self.botones.clear()

    def buena(self):
        self.aciertos += 1
        self.botones.clear()
        self.elems.clear()

        # termino la jugada y gano
        if( self.aciertos == self.maxAc):
            print("Ganaste!")
            pass