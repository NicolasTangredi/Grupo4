import pandas as pd
import matplotlib as mp
from ..Handlers import clases 

def preview_game_num():
    """retorna el numero de la ultima partida jugada"""
    df =  pd.read_csv('./data/stats.csv', encoding="utf8")
    x = sorted(df["Partida"],reverse=True)[0]
    return x

def primera_palabra():
    ds = pd.read_csv('./data/stats.csv', "r+")
    cant = ds.groupby(["estado"])["palabra"].count()
    topTen = cant.sort_values(ascending = False).head(10)
    return topTen


