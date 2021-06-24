import pandas as pd

def preview_game_num():
    """retorna el numero de la ultima partida jugada"""
    df =  pd.read_csv('./data/registro_partidas.csv', encoding="utf8")
    x = sorted(df["Partida"],reverse=True)[0]
    return x
