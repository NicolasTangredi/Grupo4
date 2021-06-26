from os import remove
import pandas as pd
from matplotlib import pyplot as pt
from ..Handlers import usuario

def preview_game_num():
    """retorna el numero de la ultima partida jugada"""
    df =  pd.read_csv('./data/stats.csv', encoding="utf8")
    x = sorted(df["Partida"],reverse=True)[0]
    return x

def primera_palabra():
    ds = pd.read_csv('./data/stats.csv', "r+")
    cant = ds.groupby(["estado"]=="inicio_de_partida")["palabra"].count()
    topTen = cant.sort_values(ascending = False).head(10)
    return topTen

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
    generos = usuario.genero()
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


    
    

