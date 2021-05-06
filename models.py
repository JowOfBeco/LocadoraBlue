from db_commands import insert, select, update, delete_data

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    insert("filmes",
           ("titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"),
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def get_filme(sigla):
    select("filmes", "sigla", sigla)

