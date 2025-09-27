from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    # Não precisa carregar JSON aqui, o HTML vai buscar direto via fetch
    return render_template("dashboard.html")

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

@app.route('/login')
def login():
    return render_template('subtelas/login.html')


if __name__ == "__main__":
    app.run(debug=True)
