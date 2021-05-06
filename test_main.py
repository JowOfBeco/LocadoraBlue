from MySQLdb import InternalError
from db_commands import execute, query, select, insert, update_2, delete_data, CONFIGURACOES_BD

CONFIGURACOES_BD = ""
CONFIGURACOES_BD = {
    "host":"localhost",
    "user":"root",
    "password":"root",
    "database":"bluecommerce_test",
}

def test_execute():
    try:
        execute("""CREATE TABLE teste (id int primary key auto_increment)""")
        execute("""DROP TABLE teste""")
        assert True
    except:
        assert False
    try:
        execute("""SHOW tables""")
        assert False
    except InternalError:
        assert True