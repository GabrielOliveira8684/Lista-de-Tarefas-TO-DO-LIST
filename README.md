# Gerenciador de Tarefas

Um gerenciador de tarefas interativo desenvolvido em Python para praticar manipulação de banco de dados, lógica de controle e organização de código. O projeto simula uma aplicação de produtividade no terminal, onde o usuário organiza sua rotina de forma simples e eficiente.

## O que ele faz?

A aplicação permite ao usuário gerenciar suas atividades diárias diretamente pelo terminal, através de um menu intuitivo.

* **Gerenciamento de tarefas:** permite adicionar, listar, marcar como concluída e excluir tarefas.
* **Listas separadas:** as tarefas são exibidas em duas listas, incompletas e completas, e a exclusão pode ser feita em qualquer uma delas.
* **Interface organizada:** limpa o terminal a cada volta ao menu e exibe um menu estruturado para facilitar a navegação.
* **Persistência de dados:** salva as tarefas automaticamente em um banco de dados SQLite (`sistema.db`), então nada se perde ao fechar o programa.
* **Tratamento de erros:** valida as opções do menu, os números das tarefas e tarefas vazias, impedindo que o programa feche sozinho caso o usuário digite algo inválido.

## Como rodar

Não é preciso instalar nada além do Python, porque o `sqlite3` já vem junto com ele.

1. Acesse a pasta do projeto:
```bash
cd TO-DO-LIST
```

2. Execute o arquivo:
```bash
python lista.py
```

O arquivo `sistema.db` é criado automaticamente na primeira execução.

## Estrutura do projeto

```text
TO-DO-LIST/
├── lista.py        # Código do gerenciador de tarefas
├── sistema.db      # Banco de dados SQLite (criado ao rodar)
└── README.md       # Documentação do projeto
```

## O que eu pratiquei e aprendi nesse projeto

Esse projeto foi importante para subir um degrau na organização de código e no uso de banco de dados com Python.

* **Banco de dados com SQLite:** uso do módulo `sqlite3` para criar a tabela de tarefas e guardar os dados de forma permanente, com `id`, `titulo` e `status`.
* **Comandos SQL:** uso de `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE` e `DELETE` para criar, listar, concluir e remover tarefas.
* **Consultas seguras:** uso de `?` nos comandos SQL para passar os valores, evitando montar o texto da consulta na mão.
* **Persistência de dados:** uso de `commit()` para salvar as alterações no banco depois de cada ação.
* **Modularização com funções:** código dividido em funções pequenas, cada uma com uma responsabilidade (validar entrada, listar tarefas, adicionar, remover, concluir), evitando repetição e facilitando a manutenção.
* **Laços de repetição e condicionais:** uso de `while` e blocos `if/elif/else` para controlar o menu principal e as ações de cada função.
* **Listas e tuplas:** uso de `fetchall()` junto com `enumerate()` para listar as tarefas numeradas e descobrir o `id` real de cada uma no banco.
* **Experiência de usuário no terminal:** uso das bibliotecas `os` e `platform` para limpar a tela em Windows e Linux/Mac, e strings de várias linhas para montar o menu.
* **Tratamento de exceções:** uso de `try/except` para validar a entrada do usuário, inclusive quando ele digita letras no lugar de números.
