from flask import Flask
import pandas as pd
from utils.analise import analisar_partidas, gerar_graficos
import os  # necessário para pegar a porta da hospedagem

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("dados/partidas.csv")
    resumo = analisar_partidas(df)
    gerar_graficos(df)
    return f"""
    <h1>🏆 Bot de Análise Pós-Jogo 🏆</h1>
    {resumo.to_frame().to_html(header=False)}
    <img src="/static/grafico_escanteios.png">
    """

# ------------------------------
# Parte final pronta para hospedar online
# ------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway ou outro serviço escolhe a porta
    app.run(host="0.0.0.0", port=port, debug=True)
