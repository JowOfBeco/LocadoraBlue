def estado_from_web(**kwargs):
    return {
        "sigla": kwargs["sigla"] if kwargs["sigla"] else "",
        "nome": kwargs["nome"] if kwargs["nome"] else "",
    }

def estado_from_db(*args):
    return {
        "sigla": args[0],
        "nome": args[1],
    }

def pais_from_web(**kwargs):
    return{
        "nome": kwargs["nome"] if kwargs["nome"] else "",
        "sigla": kwargs["sigla"] if kwargs["sigla"] else "",
    }
def pais_from_db(*args):
    return {
        "nome": args[0],
        "sigla": args[1],
    }