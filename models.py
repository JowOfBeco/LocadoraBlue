from main import insert, select

def insert_estado(sigla, nome):
    insert("estados", ["sigla", "nome"], [sigla, nome])

def get_estado(sigla):
    select("estados", "sigla", sigla)

def insert_pais(nome, sigla):
    insert("estados", ["sigla", "nome"], [sigla, nome])

def get_pais(sigla):
    select("estados", "sigla", sigla)

