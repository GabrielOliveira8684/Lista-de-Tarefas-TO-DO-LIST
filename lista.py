import sqlite3
import os
import platform
import json

conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

cursor.execute(""" 
    create table if not exists tarefas (
        id integer primary key autoincrement,
        titulo text not null,
        status text default 'pendente'
    )
""")

def salvar_dados():
    conexao.commit()


def pedir_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('\nDigite um número válido!')


def confirmar_sucesso(mensagem):
    print(f'\n{mensagem} Pressione Enter...')
    input()


def pausar():
    print('\nPressione Enter...')
    input()


def listar_incompletas():
    print('\nTarefas Incompletas:')
    cursor.execute("SELECT id, titulo FROM tarefas WHERE status = 'pendente'")
    tarefas = cursor.fetchall()
    
    if not tarefas:
        print('Nenhuma tarefa incompleta encontrada.')
        return

    for i, (id_tarefa, titulo) in enumerate(tarefas):
        print(f'{i + 1} - {titulo}')


def listar_completas():
    print('\nTarefas Completas:')
    cursor.execute("SELECT id, titulo FROM tarefas WHERE status = 'concluida'")
    tarefas = cursor.fetchall()
    
    if not tarefas:
        print('Nenhuma tarefa completa encontrada.')
        return

    for i, (id_tarefa, titulo) in enumerate(tarefas):
        print(f'{i + 1} - {titulo}')


def listar_tarefas():
    listar_incompletas()
    listar_completas()
    pausar()


def adicionar_tarefa():
    nova_tarefa = input('\nDigite a tarefa: ')
    if not nova_tarefa:
        confirmar_sucesso('Tarefa inválida!')
        return
    cursor.execute('insert into tarefas (titulo) values (?)', (nova_tarefa,))
    salvar_dados()
    confirmar_sucesso('Tarefa adicionada com sucesso!')


def remover_tarefa():
    while True:
        qual_lista = pedir_numero(
'''
Remover de qual lista: 

1 - Incompletas
2 - Completas

Digite aqui: 
'''
)

        if qual_lista not in [1, 2]:
            confirmar_sucesso('Opção inválida!')
            continue

        if qual_lista == 1:
            status_alvo = 'pendente'
            print('\nTarefas Incompletas')
        else:
            status_alvo = 'concluida'
            print('\nTarefas Completas')

        cursor.execute('select id, titulo from tarefas where status = ?', (status_alvo,))
        tarefas_db = cursor.fetchall()

        if not tarefas_db:
            if qual_lista == 1:
                confirmar_sucesso('Lista de tarefas incompletas vazia!')
            else:
                confirmar_sucesso('Lista de tarefas completas vazia!')
            return

        for i, (id_tarefa, titulo) in enumerate(tarefas_db):
            print(f'{i + 1} - {titulo}')

        remover = pedir_numero('\nQual deseja retirar (digite o número da lista): ')

        if remover <= 0 or remover > len(tarefas_db):
            confirmar_sucesso('Escolha um número válido!')
        else:
            id_real = tarefas_db[remover - 1][0]
            
            cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_real,))
            salvar_dados()
            confirmar_sucesso('Tarefa removida com sucesso!')
            return


def concluir_tarefa():
    while True:
        cursor.execute("SELECT id, titulo FROM tarefas WHERE status = 'pendente'")
        tarefas_db = cursor.fetchall()

        if not tarefas_db:
            confirmar_sucesso('Lista de tarefas incompletas vazia!')
            return
        
        listar_incompletas()

        concluir = pedir_numero('\nQual tarefa foi concluída: ')

        if concluir <= 0 or concluir > len(tarefas_db):
            confirmar_sucesso('Escolha um número válido!')
            continue

        id_real = tarefas_db[concluir - 1][0]

        cursor.execute("update tarefas set status = 'concluida' where id = ?", (id_real,))
        salvar_dados()
        
        confirmar_sucesso('Tarefa marcada como concluída!')
        return


def main():
    while True:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        print("""
    ====================================
            GERENCIADOR DE TAREFAS     
    ====================================
    1 - Adicionar Nova Tarefa
    2 - Listar Todas as Tarefas
    3 - Excluir Tarefa
    4 - Marcar Tarefa Como Concluída
    5 - Sair
    ====================================
    """)
        escolha = pedir_numero('Escolha uma opção (1-5): ')

        if escolha not in [1, 2, 3, 4, 5]:
            print('Número inválido! Pressione Enter para continuar...')
            input()
        elif escolha == 1:
            adicionar_tarefa()
        elif escolha == 2:
            listar_tarefas()
        elif escolha == 3:
            remover_tarefa()
        elif escolha == 4:
            concluir_tarefa()
        elif escolha == 5:
            break


if __name__ == '__main__':
    main()