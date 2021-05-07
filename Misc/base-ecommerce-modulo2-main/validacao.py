from models import get_estado

def valida_estado(sigla, nome):
    if len(sigla) != 2:
        return False

    if len(nome) == 0:
        return False

    return True

def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True
