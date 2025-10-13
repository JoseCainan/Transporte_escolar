import os
import json
from flask import Flask, render_template, request, redirect, jsonify


app = Flask(__name__)

def carregar_dados():
    caminho = os.path.join(app.root_path, "data", "dados.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')

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

@app.route("/adicionar_motorista", methods=["POST"])
def adicionar_motorista():
    caminho = os.path.join(app.root_path, "data", "dados.json")
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    novo = {
        "nome": request.form["nome"],
        "telefone": request.form["telefone"],
        "cnh": request.form["cnh"],
        "categoria": request.form["categoria"],
        "status": request.form["status"]
    }

    dados.setdefault("motoristas", []).append(novo)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    return redirect("/motoristas")


@app.route("/dashboard")
def dashboard():
    dados = carregar_dados()
    return render_template("dashboard.html", dados=dados)

@app.route("/veiculos")
def veiculos():
    dados = carregar_dados()
    return render_template("veiculos.html", veiculos=dados["veiculos"])

@app.route("/rotas")
def rotas():
    dados = carregar_dados()
    return render_template("rotas.html", rotas=dados["rotas_detalhadas"])

@app.route("/despesas")
def despesas():
    dados = carregar_dados()
    return render_template("despesas.html", despesas=dados["despesas"])

@app.route("/motoristas")
def motoristas():
    with open(os.path.join(app.root_path, "data", "dados.json"), "r", encoding="utf-8") as f:
        dados = json.load(f)
    return render_template("motoristas.html", motoristas=dados.get("motoristas", []))


if __name__ == "__main__":
    app.run(debug=True)
