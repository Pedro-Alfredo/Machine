from flask import Flask, request, jsonify, render_template
import pandas as pd
from app.ia import IAMaquina
from app.seguranca import Seguranca
from app.monitoramento import Monitoramento
from app.avaliacao import Avaliacao

def create_app():
    app = Flask(__name__)

    ia = IAMaquina()
    seguranca = Seguranca()
    monitor = Monitoramento()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/login", methods=["POST"])
    def login():
        senha = request.json.get("senha")
        return {"autenticado": seguranca.autenticar(senha)}

    @app.route("/analise", methods=["POST"])
    def analise():
        dados = request.json.get("dados")
        df = pd.DataFrame(dados)
        ia.analisar(df)
        return {"decisao": ia.decisao()}

    @app.route("/monitoramento")
    def monit():
        return jsonify(monitor.listar())

    @app.route("/avaliar", methods=["POST"])
    def avaliar():
        valores = request.json.get("valores")
        a = Avaliacao(valores)
        return {"media": a.media()}

    return app
