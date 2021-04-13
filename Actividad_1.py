def punto_1(tabla):
    
    def promedio_options(pal):
        if pal == "Si":         
            return print("Promedio :"," "*9,promedio) 
        elif pal == "No":
            return print("No se requiere dato")
        else:
            return print("La palabra ingresada fue incorrecta")
    def total_options(pal):
        if pal == "Si":         
            print("Suma :"," "*13,total)  
        elif pal == "No":
            print("No se requiere dato")
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
    def suma_de_notas (tabla):
        for n in tabla:
            tabla[n][2] = tabla[n][0] + tabla[n][1]          
    def sacarPromTot (tabla):
        p=0
        promedio=0
        total=0
        for a in tabla:
            total= total + int(tabla[a][2])
            p=p+1
        promedio= total/p
        return (promedio,total)
    suma_de_notas(tabla)                                    
    promedio=0
    total=0 
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

    return tabla
