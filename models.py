from db_commands import insert, select, update, delete_data, search_data

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]

def select_usuario(nome_completo):
    return search_data("usuarios", "nome_completo", nome_completo)

def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])

def delete_usuario(id):
    delete_data("usuarios", "id", id)

def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo",], [nome_completo,])

def get_diretor(id_diretor):
    return select("diretores", "id", id_diretor)[0]

def select_diretor(nome_completo):
    return search_data("diretores", "nome_completo", nome_completo)

def update_diretor(id_diretor, nome_completo, CPF):
    update("diretores", "id", id_diretor, ["nome_completo", "CPF"], [nome_completo, CPF])

def delete_diretor(id):
    delete_data("diretores", "id", id)

def insert_genero(nome):
    return insert("generos", ["nome",], [nome,])

def get_genero(id_genero):
    return select("generos", "id", id_genero)[0]

def select_genero(nome):
    return search_data("generos", "nome", nome)

def update_genero(id_genero, nome):
    update("generos", "id", id_genero, ["nome",],[nome,])

def delete_genero(id):
    delete_data("generos", "id", id)

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
                  [titulo, ano, classificacao, preco, diretores_id, generos_id])
def get_filme(id_filme):
    return select("filmes", "id", id_filme)[0]

def select_filme(titulo):
    return search_data("filmes", "titulo", titulo)

def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [id, titulo, ano, classificacao, preco, diretores_id, generos_id])

def delete_filme(id):
    delete_data("filmes", "id", id)

def insert_locacao(data_inicio, data_fim, filmes_id, id_usuario):
    return insert("locacoes", ["data_inicio", "data_fim", "filmes_id", "id_usuario"],
                  [data_inicio, data_fim, filmes_id, id_usuario])
def get_locacao(id):
    return select("locacoes", "id", id)[0]