from main import insert, select, update, delete, select_like

def insert_estado(sigla, nome):
    return insert("estados", ["sigla", "nome"], [sigla, nome])

def update_estado(id, sigla, nome):
    update("estados", "id", id, ["sigla", "nome"], [sigla, nome])

def get_estado(id_estado):
    return select("estados", "id", id_estado)[0]

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]

def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])

def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)

def select_usuarios(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)