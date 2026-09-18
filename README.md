# Gerenciador de Tarefas

Um gerenciador de tarefas interativo desenvolvido em Python para consolidar conceitos de manipulação de dados, persistência de arquivos e lógica de controle. O projeto foi estruturado para simular uma aplicação real de produtividade no terminal, garantindo que o usuário possa organizar sua rotina de forma simples e eficiente.

## O que ele faz?

A aplicação permite ao usuário gerenciar suas atividades diárias diretamente pelo terminal através de um menu intuitivo.
* **Gerenciamento Completo (CRUD):** Permite criar, visualizar, marcar como concluída e excluir tarefas da lista.
* **Interface Organizada:** Limpa o terminal e exibe um menu bem estruturado para fácil navegação.
* **Persistência de Dados:** Salva as tarefas automaticamente em um arquivo JSON para que os dados não se percam ao fechar o programa.
* **Tratamento de Erros:** Validação de opções do menu e índices de tarefas, impedindo que o programa feche sozinho caso o usuário digite algo inválido.

## Como rodar

Se você tiver o Python instalado na sua máquina, siga os passos abaixo:

1. Acesse a pasta do projeto:
```bash
cd TO-DO-LIST
```

2. Execute o arquivo:
```bash
python lista.py
```

## O que eu pratiquei e aprendi nesse projeto

Esse projeto foi fundamental para subir um degrau na organização de código e manipulação de coleções em Python:

* **Manipulação de Estruturas de Dados:** Uso de dicionários para armazenar tarefas em duas categorias (Completas e Incompletas) e listas para armazenar cada tarefa.
* **Modularização com Funções:** Código dividido em funções pequenas, cada uma com uma única responsabilidade (validar entrada, exibir listas, salvar dados, executar ações do menu), evitando repetição e facilitando manutenção.
* **Manipulação de Arquivos (I/O):** Uso de JSON para persistência de dados, lendo e escrevendo dados externos com `json.load()` e `json.dump()`.
* **Laços de Repetição e Condicionais:** Uso de loops `while` e blocos `if/elif/else` para controlar o fluxo do menu principal e das ações internas de cada função.
* **Experiência de Usuário no Terminal:** Uso da biblioteca `os` e `platform` para limpar a tela de forma multiplataforma (Windows e Linux/Mac) e formatação de strings para criar menus visuais.
* **Tratamento de Exceções:** Captura de erros com `try/except` para validação de entrada do usuário (inclusive letras digitadas no lugar de números) e manipulação de índices fora do intervalo da lista.

Valeu!