def reportes (datos):
    """ 
        Recibe como parametro un diccionario "datos" 

        La funcion pide que se elija sobre que valores se hara el reporte:
        1 --> eval1
        2 --> eval2
        3 --> suma de notas
         
        Luego pide que se ingrese un rango sobre el cual operar e informar que alumnos
        se encuentran en ese rango """
    
    print ('-' * 52)
    print ('Elija sobre que notas quiere el reporte: \n')
    print ("1 : sobre eval1")
    print ("2 : sobre eval2")
    print ("3 : sobre suma de ambas notas")
    print ('-' * 52)
    choice =  int(input ())
    print ('-' * 52)
    min = int(input('ingrese el valor minimo del rango con el que quiere operar \n'))
    max = int(input('ingrese el valor minimo del rango con el que quiere operar \n'))
    

    def rep_eval1(datos, min, max):
        """ Recibe un diccionario que que tiene como claves los nombres de los alumnos
            y el valor minimo y maximo del rango. Si la nota de la eval1 se encuentra dentro de ese rango 
            imprime el nombre del alumno """
        for n in datos:
            if datos[n][0] >= min and datos[n][0] <= max:
                print (n)

    def rep_eval2(datos, min, max):
        """ Recibe un diccionario que que tiene como claves los nombres de los alumnos
            y el valor minimo y maximo del rango. Si la nota de la eval2 se encuentra dentro de ese rango 
            imprime el nombre del alumno """
        for n in datos:
            if datos[n][1] >= min and datos[n][1] <= max:
                print (n)

    def rep_suma_tot(datos, min, max):
        """ Recibe un diccionario que que tiene como claves los nombres de los alumnos
            y el valor minimo y maximo del rango. Si la nota de la suma de notas se encuentra dentro de ese rango 
            imprime el nombre del alumno """
        for n in datos:
            if datos[n][2] >= min and datos[n][2] <= max:
                print  (n)
    
    corte = True
    print ('-' * 52)
    print ('Alumnos que tienen sus nota entre el rango ingresado:')
    while corte:
        if (choice == 1):
            rep_eval1(datos,min,max)
            corte = False
        elif (choice == 2):
            rep_eval2(datos,min,max)
            corte = False
        elif (choice == 3):
            rep_suma_tot(datos,min,max)
            corte = False
        else:
            print ('El valor ingresado no es valido, por favor vuelva a ingresar un valor valido')
            choice =  input ()
    print ('-' * 52)












    