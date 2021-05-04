from flask import Flask, jsonify, request
from main import query, execute
from decimal import Decimal
from models import insert_estado, get_estado, insert_pais, get_pais
from serializadores import estado_from_web, estado_from_db, pais_from_web, pais_from_db
from validacao import valida_estado, valida_pais



app = Flask(__name__)

@app.route("/estados", methods=["POST"]) # 1 - Checa a rota
def inserir_estado():
    estado = estado_from_web(**request.json) # 3 - formata o que vem da internet
    if valida_estado(**estado): # 2 - checa se os valores que vieram da internet são validos
        insert_estado(**estado) # 4- manda inserir o estado no banco de dados
        estado_criado = get_estado(estado["sigla"]) # 5- puxa estado criado do banco de dados
        return jsonify(estado_from_db(estado_criado)) # 6 - retorna estado formatado pro usuário
    else:
        return jsonify({"erro": "estado inválido"})

@app.route("/paises", methods =["POST"])
def inserir_pais():
    pais = pais_from_web(**request.json)
    if valida_pais(**pais):
        insert_pais(**pais)
        pais_criado = get_pais(pais["sigla"])
        return jsonify(pais_from_db(pais_criado))
    else:
        return jsonify({"erro": "pais inválido"})



def cria_estado():
    #movido pra estado_from_web
    sigla = request.json["sigla"]
    nome = request.json["nome"]

    # movido pra insert_estado
    insert("estados", ["sigla", "nome"], [sigla, nome])

    # movi para get_estado
    estado = select("estados", "sigla", sigla)

    # melhorei usando estado_from_db
    return jsonify(estado)



@app.route("/estados/<int:id>", methods=["PUT"])
def alterar_estado(id):
    pass

@app.route("/estados/<int:id>", methods=["DELETE"])
def apagar_estado(id):
    pass

@app.route("/estados", methods=["GET"])
def listar_estados():
    pass