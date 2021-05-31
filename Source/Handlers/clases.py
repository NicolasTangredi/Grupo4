

class Jugada():
    ''' es el controlador de la jugada, lleva la cuenta de los 
        elementos clickeados y si son iguales.
        para agregar un elemento se hace obj.update( boton, dato del boton )
        para reiniciar los elementos se hace obj.limpiar( tipo de dato )
    '''

    def __init__(self, coincidencias):
        self.elems = []
        self.botones = []
        self.max = coincidencias

    def update(self, boton, dato):
        ''' recibe el boton que fue clickeado y sus datos para
            chequear que sean iguales y si tiene todas las coincidencias
        '''
        self.elems.append(dato)
        self.botones.append(boton)
        esIgual = self.elems.count(self.elems[0]) == len(self.elems)

        if( not esIgual):
            return False
        elif ( len(self.elems) == self.max):
            return True

    def mala(self, tipo):
        ''' pone los casilleros en blanco y reinicia los elementos y botones guardados
        '''
        self.elems = []
        for boton in self.botones:
            if(tipo == 'imagenes'):
                boton.Update(image_data="", image_size=(100,100), disabled=False)
            else:
                boton.Update("", disabled=False)
        self.botones = []
