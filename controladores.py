from flask import Flask, jsonify, request
from models import *
from serializadores import *
from validacao import *
app = Flask(__name__)


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro":"Usuário Inválido."})

@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuario(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)

@app.route("/usuarios/<int:id>", methods=["PATCH", "PUT"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro":"Este usuário é inválido."})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return None, 204
    except:
        return jsonify({"erro": "Não foi possivel excluir este usuário, existem itens conectados a ele."})

@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        id_diretor = insert_diretor(**diretor)
        diretor_cadastrado = get_diretor(id_diretor)
        return diretor_from_db(diretor_cadastrado)
    else:
        return jsonify({"erro": "Diretor Inválido."})

@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    nome_completo = diretor_from_web(**request.args)
    diretores = select_diretor(nome_completo)
    diretores_from_db = [diretor_from_db(diretor) for diretor in diretores]
    return jsonify(diretores_from_db)

@app.route("/diretores/<int/id>", methods=["PATCH", "PUT"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        diretor_cadastrado = get_diretor(id)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro":"Diretor Inválido."})

@app.route("/diretores/<int/id>", methdos=["DELETE"])
def apagar_diretores(id):
    try:
        delete_diretor(id)
        return None, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir este usuário, existem itens conectados a ele."})

@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_cadastrado = get_genero(id_genero)
        return genero_from_db(genero_cadastrado)
    else:
        return jsonify({"erro": "Genero Inválido."})

@app.route("/generos", methods=["GET"])
def buscar_generos():
    nome_genero = genero_from_web(**request.args)
    generos = select_genero(nome_genero)
    generos_from_db = [genero_from_db(genero) for genero in generos]
    return jsonify(generos_from_db)

@app.route("/generos/<int/id>", methods=["PATCH", "PUT"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_cadastrado = get_genero(id)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro":"Genero Inválido."})

@app.route("/generos/<int/id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return None, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir este genero, existem itens conectados a ele."})

@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        id_filme = insert_filme(**filme)
        filme_cadastrado = get_filme(id_filme)
        return filme_from_db(filme_cadastrado)
    else:
        return jsonify({"erro":"Filme Inválido."})

@app.route("/filmes", methods=["GET"])
def buscar_filmes():
    titulo_filme = filme_from_web(**request.args)
    filmes = select_filme(titulo_filme)
    filmes_from_db = [filme_from_db(filme) for filme in filmes]
    return jsonify(filmes_from_db)

@app.route("/filmes<int/id>",methods=["PATCH", "PUT"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        update_filme(id, *filme)
        filme_cadastrado = get_filme(id)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro":"Filme Inválido."})

@app.route("/filmes<int/id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return None, 204
    except:
        return jsonify({"erro":"Não foi possivel excluir esse filme, existem itens conectados a ele."})

@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = locacao_from_web(**request.json)
    if valida_locacao(**locacao):
        id_locacao = insert_locacao(**locacao)
        locacao_cadastrada = get_locacao(id_locacao)
        return locacao_from_db(locacao_cadastrada)
    else:
        return jsonify({"erro":"Locação Inválida."})


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
