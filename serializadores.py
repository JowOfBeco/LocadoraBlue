def usuario_from_db(args):
    return {
        "sigla": args["sigla"],
        "nome" : args["nome"],
    }

def usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""









"""def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else ""
    }


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
        "titulo": args["titulo"],
        "ano": args["ano"],
        "classificacao": args["classificacao"],
        "preco":args["preco"],
        "diretores_id": args["diretores_id"],
        "generos_id": args["generos_id"]
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

def delete_id_from_web(**kwargs):
    return {
        "id": kwargs["id"] if kwargs["id"] else ""
    }


def delete_id_from_db(*args):
    return {
        "id": args[0]
    }"""