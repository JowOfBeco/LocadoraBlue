
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
