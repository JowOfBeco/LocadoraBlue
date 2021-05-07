from flask import Flask, jsonify, request
from main import query, execute
from decimal import Decimal
from models import insert_estado, get_estado, insert_usuario, get_usuario, update_usuario, delete_usuario, select_usuarios
from serializadores import estado_from_web, estado_from_db, usuario_from_web, usuario_from_db, nome_usuario_from_web
from validacao import valida_estado, valida_usuario


app = Flask(__name__)


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})

@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return None, 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})

@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

# # @app.route("/estados/<int:id>", methods=["PUT"])
# # def alterar_estado(id):
# #     estado = estado_from_web(**request.json)  # 3 - formata o que vem da internet
# #     if valida_estado(**estado):  # 2 - checa se os valores que vieram da internet são validos
# #         update_estado(id, **estado)  # 4- manda inserir o estado no banco de dados
# #         estado_criado = get_estado(id)  # 5- puxa estado criado do banco de dados
# #         return jsonify(estado_from_db(estado_criado))  # 6 - retorna estado formatado pro usuário
# #     else:
# #         return jsonify({"erro": "estado inválido"})
#
#
#
#
# def cria_estado():
#     #movido pra estado_from_web
#     sigla = request.json["sigla"]
#     nome = request.json["nome"]
#
#     # movido pra insert_estado
#     insert("estados", ["sigla", "nome"], [sigla, nome])
#
#     # movi para get_estado
#     estado = select("estados", "sigla", sigla)
#
#     # melhorei usando estado_from_db
#     return jsonify(estado)
#
#
#
# @app.route("/estados/<int:id>", methods=["PUT"])
# def alterar_estado(id):
#     pass
#
# @app.route("/estados/<int:id>", methods=["DELETE"])
# def apagar_estado(id):
#     pass
#
# @app.route("/estados", methods=["GET"])
# def listar_estados():
#     pass