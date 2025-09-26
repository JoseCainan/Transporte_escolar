from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    dados = {
        "alunos": 9999,
        "novos_alunos": 120,
        "escolas": 35,
        "frequencia": [5, 9, 7, 10, 6],   
        "faltas": [2, 3, 4, 1, 5],        
        "rotas": [80, 15, 5]              
    }
    return render_template("dashboard.html", dados=dados)

@app.route("/veiculos")
def veiculos():
    return render_template("veiculos.html")

@app.route("/rotas")
def rotas():
    return render_template("rotas.html")


@app.route("/despesas")
def despesas():
    return render_template("despesas.html")

@app.route('/comecar')
def comecar():
    return render_template('comecar.html')



if __name__ == "__main__":
    app.run(debug=True)
