
def ordenar(datos):
    """ 
        Ordena un diccionario segun el criterio que se elija 
        de los listados en el menu

        llamado: ordenar(diccionario)
    """
    def print_menu():
        print('elija un criterio para ordenar')
        print('    0: por nombre')
        print('    1: por la nota de la evaluacion 1')
        print('    2: por la nota de la evaluacion 2')
        print('    3: por la suma de ambas evaluaciones')

    # convierte a lista, ordena y devuelve un diccionario
    def ordenar(datos, num):
        lista = list(datos.items())

        if num != -1:
            lista.sort(key = lambda lista: lista[1][num])
        else:
            lista.sort()

        return dict(lista)
    
    print_menu()
    return ordenar( datos, int(input()) - 1 )

# prueba
if __name__ == '__main__':
    print(ordenar({
        'Agustin': [81, 30, 111], 'Alan': [60, 95, 155], 
        'Andrés': [72, 28, 100], 'Ariadna': [24, 84, 108], 
        'Bautista': [15, 84, 99], 'CAROLINA': [91, 43, 134], 
        'CESAR': [12, 66, 78], 'David': [70, 51, 121]
    }))
