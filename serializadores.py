def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "titulo" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else ""
    }

def filme_from_db(*args):
    return {
        "titulo": args[0],
        "ano": args[0],
        "classificacao": args[0],
        "preco":args[0],
        "diretores_id": args[0],
        "generos_id": args[0]
    }

def pais_from_web(**kwargs):
    return{
        "nome": kwargs["nome"] if "nome" in kwargs else "",
        "sigla": kwargs["sigla"] if "sigla" in kwargs else "",
    }
def pais_from_db(*args):
    return {
        "nome": args[0],
        "sigla": args[1],
    }
