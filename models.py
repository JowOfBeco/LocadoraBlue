from db_commands import insert, select, update, delete_data, search_data

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]

def select_usuario(nome_completo):
    return search_data("usuarios", "nome_completo", nome_completo)















"""
def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    insert("filmes",
           ("titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"),
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def select_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    select("filmes", ("titulo", "ano", "clsssificao", "preco", "diretores_id", "generos_id"),
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def delete_filme(id):
    delete_data("filmes", "id", id)

def insert_usuario(nome_completo, CPF):
    pass"""