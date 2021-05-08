def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else ""
    }

def usuario_from_db(args):
    return {
        "id": args["id"],
        "nome_completo": args["nome_completo"],
        "CPF": args["CPF"],
    }

def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""


def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }

def diretor_from_db(args):
    return {"id": args["id"],
            "nome_completo": args["nome_completo"],
            }

def genero_from_web(**kwargs):
    return kwargs["nome"] if "nome" in kwargs else ""

def genero_from_db(args):
    return {
        "id": args["id"],
        "nome": args["nome"],
    }

def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": str(kwargs["preco"]) if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else "",
    }

def filme_from_db(args):
    return{
        "id": args["id"],
        "titulo": args["titulo"],
        "ano": args["ano"],
        "classificacao": args["classificacao"],
        "preco": args["preco"],
        "diretores_id": args["diretores_id"],
        "generos_id": args["generos_id"],
    }

def locacao_from_web(**kwargs):
    return {
        "data_inicio": kwargs["data_inicio"] if "data_inicio" in kwargs else "",
        "data_fim": kwargs["data_fim"] if "data_fim" in kwargs else "",
        "filmes_id": kwargs["filme_id"] if "filmes_id" in kwargs else "",
        "id_usuario": kwargs["id_usuario"] if "id_usuario" in kwargs else "",
    }

def locacao_from_db(args):
    return {
        "id": args["id"],
        "data_inicio": args["data_inicio"],
        "data_fim": args["data_fim"],
        "filmes_id": args["filmes_id"],
        "id_usuario": args["id_usuarios"],

    }
#        TODO: Criar CHAVE ESTRANGEIRA de pagamentos em locacoes !!

#"": kwargs[""] if "" in kwargs else "",
