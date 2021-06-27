import pandas as pd
import json
import PySimpleGUI as sg
import PySimpleGUI as sg
from os import remove
from matplotlib import pyplot as pt

def primera_palabra():
    ds = pd.read_csv('./data/stats.csv',encoding="utf8")
    cant = ds.groupby(["evento"])["palabra"].count()
    return cant

def armarTop10(top10):
    return top10.plot(kind = "pie")

def cant_fin():
    ds = pd.read_csv('./data/stats.csv',encoding="utf8")
    cant = ds[ds["estado"]=="abandonada"]["cant_elementos"].count()
    cant2 = ds[ds["estado"]=="timeout"]["cant_elementos"].count()
    cant3 = ds[ds["estado"]=="finalizada"]["cant_elementos"].count()
    return cant,cant2,cant3

def porcentaje():
    pt.clf()
    etiquetas = ["abandonada","timeout","finalizada"]
    x,y,z=cant_fin()
    data_dibujo = [x,y,z]
    pt.pie(data_dibujo , labels=etiquetas, autopct='%1.1f%%',
    shadow=True, startangle=90, labeldistance= 1.1)
    pt.axis('equal')
    pt.legend(etiquetas)
    pt.title("Cantida de partidas finalzadas,abandonadas y timeout")
    pt.savefig("grafico.png",format="png")

def cant_genero():
    ds = pd.read_csv('./data/stats.csv',encoding="utf8")
    cant = ds["genero"][ds["estado"]== "finalizada"].count()
    return cant

def porcentaje2():
    pt.clf()
    etiquetas = ["Masculino","Femenino","Tejon"]
    x=cant_genero()
    data_dibujo = [x]
    pt.pie(data_dibujo ,colors=["lightblue","pink","lightgreen"], autopct='%1.1f%%',
    shadow=True, startangle=90, labeldistance= 1.1)
    pt.axis('equal')
    pt.legend(etiquetas)
    pt.title("Porcentaje de partidas finalizadas")
    pt.savefig("grafica.png",format="png")


def genero():
    with open("data/usuarios.json","r", encoding="utf8") as usuario:
            datos = json.load(usuario)
            gender = []
            for buscar_usuario in datos:
                if buscar_usuario["genero"] not in gender:
                    gender.append(buscar_usuario["genero"])                   
    return gender

def cant_genero():
    ds = pd.read_csv('./data/stats.csv',encoding="utf8")
    generos = genero()
    cant = []
    for k in generos:
        cant.append(ds[(ds["estado"] == "finalizada") & ((ds["genero"] == k) | (ds["edad"] == k))]["estado"].count())
    return generos,cant

def porcentaje2():
    pt.clf()
    etiquetas,data_dibujo = cant_genero()
    colores = ["lightblue","yellow","lightgreen","grey","red","brown","orange","lightpink","pink","purple"]
    colores2 = []
    for k in range(0,len(etiquetas)):
        colores2.append(colores[k])
    pt.pie(data_dibujo ,colors=colores2, autopct='%1.1f%%',
    shadow=True, startangle=90, labeldistance= 1.1)
    pt.axis('equal')
    pt.legend(etiquetas)
    pt.title("Porcentaje de partidas finalizadas")
    pt.savefig("grafica.png",format="png")

def build_estad(ganadas,perdidas,puntaje):
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.T("Porcentaje de partidas abandonadas,finalizadas y timeout")],
              [sg.Button("a ver pa")],
            [sg.T("Porcentaje de partidas finalizadas por genero")],
            [sg.Button("mostra compa")],
              [sg.Button("Ok")]
              ]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window

def build_graph2():
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.Image("grafica.png")],
              [sg.Button("Ok")]]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window

def stats_logged():
    """devuelve las estadisticas del usuario conectado"""
    
    with open('data/usuarios.json',"r", encoding="utf8") as usuar:
        usuar = json.load(usuar)

        for usuario in usuar:
            if usuario["conectado"] == 1:
                num1 = usuario["estadisticas"]["partidas_ganadas"]
                num2 = usuario["estadisticas"]["partidas_perdidas"]
                num3 = usuario["estadisticas"]["puntaje_maximo"]
        
        return num1,num2,num3
    
def start():
    "Ejecuta la ventana de estadisticas del menu principal "

    window = loop()
    window.close()
    
def loop():
    num1,num2,num3 = stats_logged()
    window = build_estad(num1,num2,num3)

    while True:
        event, _values = window.read()
        
        if event == "a ver pa":
            porcentaje()
            start2()
            break
        
        if event == "mostra compa":
            porcentaje2()
            start3()
            break
        
        if event == "Ok" or event == None:
            break
        
    return window

def build_graph1():
    "Construye la ventana de estadisticas del usuario"
    
    layout = [[sg.Image("grafico.png")],
              [sg.Button("Ok")]
              ]
    
    window = sg.Window('Estadisticas', layout, element_justification='center') 
    return window

def start2():
    "Ejecuta la ventana de estadisticas del menu principal "

    window = loop2()
    window.close()
def loop2():
    window = build_graph1()

    while True:
        event, _values = window.read()
         
        if event == "Ok" or event == None:
            break
        
    return window

def start3():
    "Ejecuta la ventana de estadisticas del menu principal "

    window = loop3()
    window.close() 
def loop3():
    window = build_graph2()

    while True:
        event, _values = window.read()
         
        if event == "Ok" or event == None:
            break
        
    return window
def cant_palabras():
    ds = pd.read_csv('./data/stats.csv',encoding="utf8")
    dic = {}
    l=0
    for k in range(l,len(ds.loc[:])):
        print(k)
        if k == 3:
            l=200
            

def top():
    ds = pd.read_csv('./data/stats.csv',encoding="utf8")
    cant = ds[(ds["estado"] == "ok") | (ds["evento"]=="inicio_partida")]
    tamaño = len(cant.iloc[:])
    dic = {}
    next_word = False
    for k in range(0,tamaño):
        if cant.iloc[k]["evento"] == "inicio_partida":
            next_word = True
        if (cant.iloc[k]["estado"] == "ok") & (next_word):
            if cant.iloc[k]["palabra"] not in list(dic.keys()):
                dic[cant.iloc[k]["palabra"]] = 0
            else:
                dic[cant.iloc[k]["palabra"]] = dic[cant.iloc[k]["palabra"]] +1
            next_word = False 
    return dic    

def convertirTop():
    f= top()
    myList = f.items()

    myList = list(myList)

    k = sorted(myList,key=lambda x: x[1] ,reverse=True)[:5]  
    return k              

print(convertirTop())