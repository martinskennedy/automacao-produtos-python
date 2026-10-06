from flask import Flask, render_template, request

app = Flask(__name__)

produtos = []

@app.route("/")
def index():
    return render_template("index.html", produtos=produtos)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    codigo = request.form["codigo"]
    nome = request.form["nome"]
    preco = request.form["preco"]
    quantidade = request.form["quantidade"]

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

    return render_template(
        "index.html",
        produtos=produtos,
        mensagem="Produto cadastrado com sucesso!"
    )

if __name__ == "__main__":
    app.run(debug=True)