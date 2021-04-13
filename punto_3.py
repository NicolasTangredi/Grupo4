
def ordenar(datos):
    """ Ordena un diccionario segun el criterio que se elija 
        de los listados en el menu """
    
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
            if num == 2 and lista[0][1][num] == -1:
                print('--! Estas tratando de ordenar por el total, pero aun no fue calculado !--')

            lista.sort(key = lambda lista: lista[1][num])
        else:
            lista.sort()

        return dict(lista)
    
    print_menu()
    return ordenar( datos, int(input()) - 1 )