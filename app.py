from decimal import Decimal

from flask import Flask, jsonify, request
from main import query, select, update_2, delete_data, insert

app = Flask(__name__)

@app.route("/paises", methods=["GET", "PATCH", "DELETE", "POST"])
def paises():
    if request.method == "GET":
        return jsonify(select("paises"))
    elif request.method == "PATCH":
        return jsonify(update_2())
    elif request.method =="DELETE":
        return jsonify(delete_data())
    elif request.method == "POST":
        return jsonify(insert())

@app.route("/estados", methods=["GET", "PATCH", "DELETE", "POST"])
def estados():
    if request.method == "GET":
        return jsonify(select("estados"))
    elif request.method == "PATCH":
        return jsonify(update_2())
    elif request.method =="DELETE":
        return jsonify(delete_data())
    elif request.method == "POST":
        return jsonify(insert())

@app.route("/cidades", methods=["GET", "PATCH", "DELETE", "POST"])
def cidades():
    a = request.json
    if request.method == "GET":
        return jsonify(select("cidades"))
    elif request.method == "PATCH":
        return jsonify(update_2())
    elif request.method =="DELETE":
        return jsonify(delete_data())
    elif request.method == "POST":
        return jsonify(insert())
    elif request.method == "POST":
        return jsonify(insert("usuarios", ("nome", "email", "senha", "telefone"),
                              (a["nome"], a["email"], a["senha"], a["telefone"])))

@app.route("/usuarios", methods=["GET", "PATCH", "DELETE", "POST"])
def usuarios():
    a = request.json
    if request.method == "GET":
        return jsonify(select("usuarios"))
    elif request.method == "PATCH":
        return jsonify(update_2("usuarios", "nome", "Johm", (), "Johmself"))
    elif request.method =="DELETE":
        return jsonify(delete_data("usuarios", "id", "1"))
    elif request.method == "POST":
        return jsonify(insert("usuarios", ("nome", "email", "senha", "telefone"),
                              (a["nome"], a["email"], a["senha"], a["telefone"])))

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_usuario_id(id):
    return jsonify(delete_data("usuarios", "id", id))

@app.route("/produtos", methods=["GET", "PATCH", "DELETE", "POST"])
def produtos():
    if request.method == "GET":
        produtos = query("SELECT * FROM produtos")
        produtos_formatados = converte_preco_em_string(produtos)
        return jsonify(produtos_formatados)
    elif request.method == "PATCH":
        return jsonify(update_2())
    elif request.method =="DELETE":
        return jsonify(delete_data())
    elif request.method == "POST":
        return jsonify(insert())

@app.route("/categorias_produto", methods=["GET", "PATCH", "DELETE", "POST"])
def categorias():
    if request.method == "GET":
        return jsonify(select("categorias_produto"))
    elif request.method == "PATCH":
        return jsonify(update_2())
    elif request.method =="DELETE":
        return jsonify(delete_data())
    elif request.method == "POST":
        return jsonify(insert())

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

def converte_preco_em_string(produto):
    return (produto[0], produto[1], produto[2], str(produto[3]))