import mysql.connector

CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "131206ic",
    "database": "gerenciador_de_tarefas"
}

def conector():
    try:
        mydb = mysql.connector.connect(**CONFIG)
        return mydb
    except mysql.connector.Error as err:
        print(f'Erro ao se conectar ao MySQL {err}')