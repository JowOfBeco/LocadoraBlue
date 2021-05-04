from mysql.connector import connect

show_schemas = "SHOW SCHEMAS"

params = None

CONFIGURACOES_BD = {
    "host":"localhost",
    "user":"root",
    "password":"root",
    "database":"bluecommerce"
}


def execute(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="bluecommerce") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()



def query(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="bluecommerce") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

def create_pais():
    execute(f"""CREATE TABLE paises(id int unsigned auto_increment not null primary key,
            id_idioma int unsigned,
            nome varchar(255) not null,
            sigla varchar(25) not null)""")

def create_estado():
    execute(f"""CREATE TABLE estados(id int unsigned auto_increment not null primary key,
                nome varchar(255) not null,
                sigla varchar(25) not null,
                id_pais int unsigned,
                codigo_ibge int unsigned not null)""")

def create_cidade():
    execute("""CREATE TABLE cidades(id int unsigned auto_increment not null primary key,
                    nome varchar(255) not null,
                    id_estado int unsigned,
                    codigo_ibge int unsigned not null)""")

def create_usuario():
    execute("""CREATE TABLE usuarios(id int unsigned auto_increment not null primary key,
                    nome varchar(255) not null,
                    email varchar(255) not null,
                    senha varchar(255) not null,
                    telefone varchar(20) default 'NULL')""")

def create_produto():
    execute(f"""CREATE TABLE produtos(id int unsigned auto_increment not null primary key,
    nome varchar(255) not null,
    descricao text not null,
    preco decimal(7,2) not null,
    id_categoria_produto int)""")

def create_cat_produto():
    execute(f"""CREATE TABLE categorias_produto(id int unsigned auto_increment not null primary key,
    nome varchar(255) not null,
    id_categoria_produto_geral int not null)""")

def create_venda():
    execute(f"""CREATE TABLE vendas(id int unsigned auto_increment not null primary key,
    data_venda date,
    id_usuario int unsigned not null)""")

def create_venda_produto():
    execute(f"""CREATE TABLE vendas_produtos(vendas_id_venda int unsigned not null primary key,
    produtos_id_produto int unsigned not null,
    quantidade int not null)""")

def create_estoque():
    execute(f"""CREATE TABLE estoques(id int unsigned not null primary key,
    quantidade int not null default 0,
    tipo varchar(255) default 'NULL')""")

def insert(tabela, colunas, valores):
    execute(f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['%s' for valor in valores])})", valores)

def search_data(nome_tabela, nome_linha, dado_linha):
    return query(f'''select * from {nome_tabela} where {nome_linha} = %s''', (dado_linha,))

def update(nome_tabela,coluna, valor, id_coluna, id_valor):
    execute(f"""UPDATE {nome_tabela} 
            SET {coluna} = %s WHERE {id_coluna} = %s""", (valor, id_valor))

def update_2(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])

def delete_data(nome_tabela, nome_coluna, coluna_valor):
    execute(f"""delete from  {nome_tabela} 
            WHERE {nome_coluna} = %s""", (coluna_valor,))

def select(tabela, chave = 1,valor_chave = 1, limit = 100, offset =0):
    return query(f"""SELECT * FROM {tabela} WHERE {chave} = %s LIMIT {limit} offset {offset}""", (valor_chave,))
