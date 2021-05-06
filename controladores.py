from flask import Flask, jsonify, request
from db_commands import query, select, update, delete_data, insert
from models import insert_filme, get_filme
from serializadores import filme_from_db, filme_from_web
from validacao import valida_filme
app = Flask(__name__)

@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        insert_filme(**filme)
        return jsonify(filme_from_db(filme))
    else:
        return jsonify({"erro": "Filme Inválido."})

#@app.route("/diretores", methods=["POST"]) # 1 - Checa a rota
#def inserir_estado():
#    estado = estado_from_web(**request.json) # 3 - formata o que vem da internet
#    if valida_estado(**estado): # 2 - checa se os valores que vieram da internet são validos
#        insert_estado(**estado) # 4- manda inserir o estado no banco de dados
#        estado_criado = get_estado(estado["sigla"]) # 5- puxa estado criado do banco de dados
#        return jsonify(estado_from_db(estado_criado)) # 6 - retorna estado formatado pro usuário
#    else:
#        return jsonify({"erro": "estado inválido"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)