from flask import Flask, jsonify, request
from db_commands import query, select, update, delete_data, insert
from models import insert_usuario, get_usuario, select_usuario
from serializadores import usuario_from_db, usuario_from_web, nome_usuario_from_web
from validacao import  valida_usuario
app = Flask(__name__)


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro":"Usuário inválido"})

@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuario(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)










"""
@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        pass

@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        id_filme = insert_filme(**filme)
        filme_criado = get_filme(id_filme)
        return jsonify(filme_from_db(filme))
    else:
        return jsonify({"erro": "Filme Inválido."})

@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    filme_id = delete_id_from_web(**request.json)
    try:
        if valida_id(id):
            delete_filme(**filme_id)
            return jsonify(delete_id_from_db(filme_id))
    except:
        return jsonify({"erro": "Não foi possível deletar esse filme."})

@app.route("/filmes/", methods=["GET"])
def get_filme():
    filme = filme_from_web(**request.json)
    filme_selecionado = select_filme(**filme)
    if filme_selecionado != None:
        return jsonify(filme_from_db(filme_selecionado))
    else: return jsonify({"erro":"Filme inválido."})
"""
#@app.route("/diretores", methods=["POST"]) # 1 - Checa a rota
#def inserir_estado():
#    estado = estado_from_web(**request.json) # 3 - formata o que vem da internet
#    if valida_estado(**estado): # 2 - checa se os valores que vieram da internet são validos
#        insert_estado(**estado) # 4- manda inserir o estado no banco de dados
#        estado_criado = get_estado(estado["sigla"]) # 5- puxa estado criado do banco de dados
#        return jsonify(estado_from_db(estado_criado)) # 6 - retorna estado formatado pro usuário
#    else:
#        return jsonify({"erro": "estado inválido"})
