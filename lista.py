import os
import platform
import json

arquivo = os.path.join(os.path.dirname(__file__), 'tarefas.json')

def salvar_dados(tarefas):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def carregar_dados():
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            tarefas = json.load(f)
    except FileNotFoundError:
        tarefas = {
            'Completas': [],
            'Incompletas': []
        }
    return tarefas

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

def listar_incompletas(tarefas):
    print('\nTarefas Incompletas: ')
    for i, tarefa_in in enumerate(tarefas['Incompletas']):
        print(f'{i + 1} - {tarefa_in}')

def listar_completas(tarefas):
    print('\nTarefas Completas: ')
    for j, tarefa_com in enumerate(tarefas['Completas']):
        print(f'{j + 1} - {tarefa_com}')

def listar_tarefas(tarefas):
    listar_incompletas(tarefas)
    listar_completas(tarefas)
    pausar()

def adicionar_tarefa(tarefas):
    nova_tarefa = input('\nDigite a tarefa: ')
    if not nova_tarefa:
        confirmar_sucesso('Tarefa inválida!')
        return
    tarefas['Incompletas'].append(nova_tarefa)
    salvar_dados(tarefas)
    confirmar_sucesso('Tarefa adicionada com sucesso!')

def remover_tarefa(tarefas):
    while True:
        qual_lista = pedir_numero('''
Remover de qual lista: 

1 - Incompletas
2 - Completas

Digite aqui: ''')

        if qual_lista not in [1, 2]:
            confirmar_sucesso('Opção inválida!')
            continue

        elif qual_lista == 1:
            if not tarefas['Incompletas']:
                confirmar_sucesso('Lista de tarefas incompletas vazia!')
                return
            listar_incompletas(tarefas)
            remover = pedir_numero('\nQual deseja retirar: ')

            if remover <= 0 or remover > len(tarefas['Incompletas']):
                confirmar_sucesso('Escolha um número válido!')
            else:
                tarefas['Incompletas'].pop(remover - 1)
                salvar_dados(tarefas)
                confirmar_sucesso('Tarefa removida com sucesso!')
                return
        else:
            if not tarefas['Completas']:
                confirmar_sucesso('Lista de tarefas completas vazia!')
                return
            listar_completas(tarefas)
            remover = pedir_numero('\nQual deseja retirar: ')

            if remover <= 0 or remover > len(tarefas['Completas']):
                confirmar_sucesso('Escolha um número válido!')
            else:
                tarefas['Completas'].pop(remover - 1)
                salvar_dados(tarefas)
                confirmar_sucesso('Tarefa removida com sucesso!')
                return

def concluir_tarefa(tarefas):
    while True:
        if not tarefas['Incompletas']:
            confirmar_sucesso('Lista de tarefas incompletas vazia!')
            return
        listar_incompletas(tarefas)
        concluir = pedir_numero('\nQual tarefa foi concluída: ')
        if concluir <= 0 or concluir > len(tarefas['Incompletas']):
            confirmar_sucesso('Escolha um número válido!')
            continue
        concluida = tarefas['Incompletas'].pop(concluir - 1)
        tarefas['Completas'].append(concluida)
        salvar_dados(tarefas)
        confirmar_sucesso('Tarefa marcada como concluída!')
        return

def main():
    tarefas = carregar_dados()

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
            adicionar_tarefa(tarefas)
        elif escolha == 2:
            listar_tarefas(tarefas)
        elif escolha == 3:
            remover_tarefa(tarefas)
        elif escolha == 4:
            concluir_tarefa(tarefas)
        elif escolha == 5:
            break

if __name__ == '__main__':
    main()