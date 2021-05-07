def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False
    if len(CPF)!= 14:
        return False
    return True












"""def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False
    return True


def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if titulo == 0:
        return False
    elif ano == 0:
        return False
    elif classificacao == 0:
        return False
    elif preco == 0:
        return False
    elif diretores_id == 0:
        return False
    elif generos_id == 0:
        return False
    return True

def valida_id(id):
    if id == 0:
        return False
    return True"""