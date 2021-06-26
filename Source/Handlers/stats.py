from os import remove
import pandas as pd
from matplotlib import pyplot as pt

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

    
porcentaje()

