nombres = """"Agustin",
    "Alan",
    "Andrés",
    "Ariadna",
    "Bautista",
    "CAROLINA",
    "CESAR",
    "David",
    "Diego",
    "Dolores",
    "DYLAN",
    "ELIANA",
    "Emanuel",
    "Fabián",
    "Facundo",
    "Facundo",
    "FEDERICO",
    "FEDERICO",
    "GONZALO",
    "Gregorio",
    "Ignacio",
    "Jonathan",
    "Jonathan",
    "Jorge",
    "JOSE",
    "JUAN",
    "Juan",
    "Juan",
    "Julian",
    "Julieta",
    "LAUTARO",
    "Leonel",
    "LUIS",
    "Luis",
    "Marcos",
    "María",
    "MATEO",
    "Matias",
    "Nicolás",
    "NICOLÁS",
    "Noelia",
    "Pablo",
    "Priscila",
    "TOMAS",
    "Tomás",
    "Ulises",
    "Yanina", """
eval1 = """81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74 """
eval2 = """30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10 """
def promedio_options(pal):
    if pal == "Si":         
        return print("Promedio :"," "*9,promedio) 
    elif pal == "No":
        return print("No te digo un carajo entonces capo")
    else:
        return print("La palabra ingresada fue incorrecta")
def total_options(pal):
    if pal == "Si":         
        print("Suma :"," "*13,total)  
    elif pal == "No":
       print("No te digo un carajo entonces capo")
    else:
        print("La palabra ingresada fue incorrecta")
def imprimirNotas(tabla):
    h=True              
    for k in tabla:
        if h:
            print("Nombres"," "*3," E1","","E2","","Suma")
            print("-"*40)
            h=False
        if len(k) == 8:
            print(k," "*2,tabla[k])
        elif len(k) == 7:
            print(k," "*3,tabla[k])
        elif len(k) == 6:
            print(k," "*4,tabla[k])
        elif len(k) == 5:
            print(k," "*5,tabla[k])
        elif len(k) == 4:
            print(k," "*6,tabla[k])
        else:
            print(k)
def asignarNotas(nombres,eval1,eval2,tabla):
    z=0   
    for i in nombres:
        i=i.replace('"',"")
        tabla[i] = [int(eval1[z]) , int(eval2[z]) , int(eval1[z]) + int(eval2[z]) ]
        z=z+1      
    print("-"*25)
def sacarPromTot (tabla):
    p=0
    promedio=0
    total=0
    for a in tabla:
        total= total + int(tabla[a][2])
        p=p+1
    promedio= total/p
    return (promedio,total)                                
nombres=nombres.replace(",","")
eval1=eval1.replace(",","")
eval2=eval2.replace(",","")
nombres = nombres.split()
eval1=eval1.split()
eval2=eval2.split() 
tabla = {}
promedio=0
total=0 
asignarNotas(nombres,eval1,eval2,tabla)
promedio,total = sacarPromTot(tabla)
pal=input("Si quiere saber el total de las notas escriba 'Si',sino,escriba 'No' : ")
pal1=input("Si quiere saber el promedio de las notas escriba 'Si',sino,escriba 'No' : ")
imprimirNotas(tabla)            
print("-"*26)        
total_options(pal)
print("-"*26)        
print("-"*39)                             
promedio_options(pal1)
print("-"*39)

def rep_eval1(datos, nombres, min, max,):
        # Recibe un diccionario que que tiene como claves los nombres de los alumnos, una lista con los nombres
        #   y un el valor minimo y el maximo del rango. Si la nota de la eval 1 se encuentra dentro de ese rango 
        #   imprime el nombre del alumno 
    for n in nombres:
        x = datos.get(n)[0]
        if x >= min and x <= max:
            print (datos.get(n)[0])

def rep_eval2(datos, nombres, min, max):
        # Recibe un diccionario que que tiene como claves los nombres de los alumnos, una lista con los nombres
        #    y un el valor minimo y el maximo del rango. Si la nota de la eval 2 se encuentra dentro de ese rango 
        #    imprime el nombre del alumno 
    for n in nombres:
        x = datos.get(n)[1]
        if x >= min and x <= max:
            print (n)

def rep_suma_tot(datos, nombres, min, max,):
        # Recibe un diccionario que que tiene como claves los nombres de los alumnos, una lista con los nombres
        #   y un el valor minimo y el maximo del rango. Si la nota de la suma de notas se encuentra dentro de ese rango 
        #   imprime el nombre del alumno
    for n in nombres:
        x = int(datos.get(n)[2])
        if (x >= min) and (x <= max):
            print (n)
            
def reportes (datos, nombres):
    # 
    #    recibe como parametro un diccionario "datos" y una lista de nombres
    #
    #    La funcuin pide que se elija sobre que valores se hara el reporte:
    #    1 --> eval1
    #    2 --> eval2
    #    3 --> suma de notas
    #    
    #    Luego  pide que se ingrese un rango sobre el cual operar e informar que alumnos
    #    se encuentran en ese rango """
    #
    
    print ('Elija sobre que notas quiere el reporte: \n')
    print ("1 : sobre eval1")
    print ("2 : sobre eval2")
    print ("3 : sobre suma de ambas notas")
    choice =  int(input ())
    min = int(input('ingrese el valor minimo del rango con el que quiere operar \n'))
    max = int(input('ingrese el valor maximo del rango con el que quiere operar \n'))    
    corte = True
    while corte:
        if (choice == 1):
            rep_eval1(datos,nombres,min,max)
            corte == False
        elif (choice == 2):
            rep_eval2(datos,nombres,min,max)
            corte == False
        elif (choice == 3):
            rep_suma_tot(datos,nombres,min,max)
            corte == False
        else:
            print ('El valor ingresado no es valido, por favor vuelva a ingresar un valor valido')
            choice =  int(input ())

reportes(tabla,nombres)

