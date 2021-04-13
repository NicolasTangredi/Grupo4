import punto_3, Actividad_1, Actividad1_reportes

# datos
nombres = [
    "Agustin", "Alan", "Andrés", "Ariadna", "Bautista",
    "CAROLINA", "CESAR", "David", "Diego", "Dolores", "DYLAN",
    "ELIANA", "Emanuel", "Fabián", "Facundo", "Facundo", "FEDERICO",
    "FEDERICO", "GONZALO", "Gregorio", "Ignacio", "Jonathan",
    "Jonathan", "Jorge", "JOSE","JUAN", "Juan", "Juan", "Julian",
    "Julieta", "LAUTARO", "Leonel","LUIS", "Luis", "Marcos",
    "María", "MATEO", "Matias","Nicolás", "NICOLÁS", "Noelia",
    "Pablo", "Priscila", "TOMAS","Tomás", "Ulises", "Yanina"
]    
eval_1 = [
    81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35,
    67, 10, 57, 11, 69, 12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10,
    87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74
]
eval_2 = [
    30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13,
    34, 96, 71, 86, 37, 64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59,
    57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10
]


# funciones 
def elegir_opcion():
    """
        imprime un menu y espera un numero 
        dentro del rango de las opciones, si el
        numero no esta en el rango debera volver
        a ingresar una opcion
    """
    def print_menu():
        print('Elija una opcion:')
        print('     0: Cerrar menu')
        print('     1: Calcular promedio total y suma de ambas notas')
        print('     2: Generar un reporte dentro de un rango')
        print('     3: Ordenar los datos')

    op = -1
    while not op in range(0,4):
        print_menu()
        op = int(input('Opcion: '))

    return op


def asignarNotas(nombres, eval_1, eval_2, tabla):
        z=0   
        for i in nombres:
            tabla[i] = [int(eval_1[z]) , int(eval_2[z]) , -1 ]
            z=z+1      

# programa principal
datos = {}
asignarNotas(nombres, eval_1, eval_2, datos)
modulos = {
    1: Actividad_1.punto_1, 
    2: Actividad1_reportes.reportes, 
    3: punto_3.ordenar
}

opcion = elegir_opcion()
while opcion != 0:
    if opcion != 3:
        modulos[opcion](datos)
    else:
        datos = modulos[opcion](datos)
    opcion = elegir_opcion()
