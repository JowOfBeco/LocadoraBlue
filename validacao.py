def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True

def valida_diretor(nome_completo):
    if len(nome_completo) == 0:
        return False

    return True

def valida_genero(nome):
    if len(nome) == 0:
        return False

    return True

def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if len(titulo) == 0:
        return False
    if ano == 0:
        return False
    if len(classificacao) == 0:
        return False
    if len(preco) == 0:
        return False
    if len(diretores_id) == 0:
        return False
    if len(generos_id) == 0:
        return False

    return True

def valida_locacao(data_inicio, data_fim, filmes_id, id_usuario):
    if data_inicio == 0:
        return False
    if data_fim == 0:
        return False
    if filmes_id == 0:
        return False
    if id_usuario == 0:
        return False

    return True