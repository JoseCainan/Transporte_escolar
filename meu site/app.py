import os
import json
from flask import Flask, render_template, request, redirect, jsonify


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alunos")
def alunos():
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    return render_template("alunos.html", escolas=dados.get("escolas", []))

@app.route("/alunos/<nome_escola>")
def alunos_por_escola(nome_escola):
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    escola = next((e for e in dados["escolas"] if e["nome"] == nome_escola), None)
    if escola:
        return jsonify({"alunos": escola.get("alunos", [])})
    return jsonify({"alunos": []})

@app.route("/adicionar_escola", methods=["POST"])
def adicionar_escola():
    nome_escola = request.form["nome_escola"]
    nome_aluno = request.form["nome_aluno"]
    rota = request.form["rota"]
    qnt_passageiros = request.form["qnt_passageiros"]
    status = request.form["status"]

    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    escola = next((e for e in dados["escolas"] if e["nome"] == nome_escola), None)
    if not escola:
        escola = {"nome": nome_escola, "alunos": []}
        dados["escolas"].append(escola)

    escola["alunos"].append({
        "nome": nome_aluno,
        "rota": rota,
        "qnt_passageiros": qnt_passageiros,
        "status": status
    })

    with open("dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    return redirect("/alunos")

@app.route("/dashboard")
def dashboard():
    # Não precisa carregar JSON aqui, o HTML vai buscar direto via fetch
    return render_template("dashboard.html")

@app.route("/veiculos")
def veiculos():
    dados = carregar_dados()
    return render_template("veiculos.html", veiculos=dados["veiculos"])

@app.route("/rotas")
def rotas():
    return render_template("rotas.html")

@app.route("/despesas")
def despesas():
    return render_template("despesas.html")

@app.route('/comecar')
def comecar():
    return render_template('comecar.html')

@app.route('/login')
def login():
    return render_template('subtelas/login.html')


if __name__ == "__main__":
    app.run(debug=True)
