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
        return None

def mostrar_menu():
    print('-------------------------------------')
    print('SISTEMA DE GERENCIAMENTO DE TAREFAS')
    print('-------------------------------------')
    print('1 - Adicionar Tarefa')
    print('2 - Listar Tarefa')
    print('3 - Concluir Tarefa (Por ID)')
    print('4 - Remover Tarefa (Por ID)')
    print('5 - Sair')
    print()
    return input('Selecione uma opção: ')


def adicionar_tarefas():
    ...

def lista_tarefas():
    ...

def concluir_tarefas():
    ...

def remover_tarefas():
    ...

def main():
    ...