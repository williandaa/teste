import pandas as pd
import matplotlib.pyplot as plt
import os

def analisar_partidas(df):
    return pd.Series({
        "média_escanteios": df["escanteios_total"].mean(),
        "média_finalizações": df["finalizacoes_total"].mean(),
        "média_posse_bola": df["posse_bola"].mean(),
        "total_jogos": len(df)
    })

def gerar_graficos(df):
    if not os.path.exists("static"):
        os.makedirs("static")
    plt.figure(figsize=(8,5))
    plt.bar(df["time_casa"], df["escanteios_total"], color="skyblue")
    plt.title("Escanteios por Time da Casa")
    plt.savefig("static/grafico_escanteios.png")
    plt.close()
