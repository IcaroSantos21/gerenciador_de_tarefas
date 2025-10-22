import mysql.connector

CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "131206ic",
    "database": "gerenciador_de_tarefas"
}

def conectar():
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

def adicionar_tarefas(descricao):
    conn = conectar()
    if conn is None: return

    cursor = conn.cursor()
    sql = "INSERT INTO tarefas (descricao) VALUES (%s)"

    try:
        cursor.execute(sql, (descricao,))
        conn.commit()
        print(f'\n[SUCESSO] Tarefa: {descricao} adiconada (ID: {cursor.lastrowid})')
    except Exception as e:
        print(f'\n[ERRO] Falha ao adicionar a tarefa: {e}')
    finally:
        conn.close()
        cursor.close()

def lista_tarefas():
    conn = conectar()
    if conn is None: return
    
    cursor = conn.cursor()
    sql = 'SELECT id_tarefas, descricao, status FROM tarefas ORDER BY data_criacao DESC'

    try:
        cursor.execute(sql)
        tarefas = cursor.fetchall()

        print('----LISTA DE TAREFAS----')
        if not tarefas:
            print('Nenhuma tarefa encontrada na lista')
            return
        for id_tarefas, descricao, status in tarefas:
            prefixo = '[✅]' if status == 'concluido' else '[]'
            print(f'{prefixo} ID: ({id_tarefas}) TAREFA: ({descricao}) STATUS: ({status})')
    except Exception as e:
        print(f'\n[ERRO] ao listar as tarefas: {e}')
    finally:
        cursor.close()
        conn.close()

def concluir_tarefas(tarefas_id):
    conn = conectar()
    if conn is None: return

    cursor = conn.cursor()
    sql = 'UPDATE tarefas SET status = "concluido" WHERE id_tarefas = %s'

    try:
        cursor.execute(sql, (tarefas_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f'\n[SUCESSO] Tarefa com o ID {tarefas_id} Concluída')
        else:
            print(f'\n[AVISO] Tarefa com o ID {tarefas_id} não encontrada')
    except Exception as e:
        print(f'\n[ERRO] Falha ao atualizar a tarefa para concluída: {e}')
    finally:
        cursor.close()
        conn.close()

def remover_tarefas(tarefas_id):
    conn = conectar()
    if conn is None: return

    cursor = conn.cursor()
    sql = 'DELETE FROM tarefas WHERE id_tarefas = %s'

    try:
        cursor.execute(sql, (tarefas_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f'\n[SUCESSO] Tarefa com o ID: {tarefas_id} excluida com sucesso')
        else:
            print(f'\n[AVISO] Tarefa com o ID: {tarefas_id} não encontrado')
    except Exception as e:
        print(f'\n[ERRO] Erro ao deletar a tarefa {e}')
    finally:
        cursor.close()
        conn.close()

def main():
    while True:
        opcao = mostrar_menu()

        if opcao == '1':
            descricao = input('Digite a descrição da tarefa que deseja adicionar: ')
            
            if descricao:
                adicionar_tarefas(descricao)
            
        elif opcao == '2':
            lista_tarefas()
        elif opcao == '3':
            try:
                id_tarefa = int(input('Digite o id da tarefa a ser concluida: '))
                concluir_tarefas(id_tarefa)
            except ValueError:
                print('\n[ERRO] O id precisa ser um número inteiro')
        elif opcao == '4':
            try:
                id_tarefa = int(input('Digite o id da tarefa a ser removida: '))
                remover_tarefas(id_tarefa)
            except ValueError:
                print('\n[ERRO] O id precisa ser um número inteiro')
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('\n[ERRO] Opção inválida')

