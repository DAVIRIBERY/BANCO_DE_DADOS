# 🏥 FaturamentoBank – Gerenciador de Convênios

## 📌 Sobre o projeto

O **FaturamentoBank** é um sistema desenvolvido em Python com integração ao banco de dados SQLite, com o objetivo de cadastrar, consultar, atualizar e visualizar informações relacionadas aos convênios médicos e suas respectivas regras de cobrança.

O projeto foi desenvolvido como prática de programação, utilizando conceitos de lógica, funções, estruturas de repetição, validação de dados e manipulação de banco de dados.

## 🚀 Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

- **1 – Cadastrar convênios:** permite cadastrar informações dos convênios, tabelas de honorários, medicamentos, materiais e quantidades permitidas de atendimentos.
- **2 – Pesquisar convênios:** permite localizar um convênio pelo nome e visualizar suas informações.
- **3 – Alterar informações:** permite atualizar informações de um convênio já cadastrado.
- **4 – Listar convênios:** apresenta todos os convênios armazenados no banco de dados.
- **5 – Sair:** encerra o programa.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **SQLite3:** banco de dados para armazenamento das informações.
- **Datetime:** utilizado para registrar a data dos cadastros.

## 🗄️ Estrutura do banco de dados

O sistema utiliza uma tabela chamada `faturamento`, composta pelos seguintes campos:

| Campo | Descrição |
|---|---|
| id | Identificador único do cadastro |
| Convenio | Nome do convênio |
| Tabela_Honorarios | Tabela de honorários médicos |
| Tabela_Medicamentos | Tabela de medicamentos acordada |
| Tabela_Materiais | Tabela de materiais acordada |
| Fisioterapia_Andares | Quantidade permitida de atendimentos |
| Fisioterapia_Uti | Quantidade permitida na UTI |
| Fonoaudiologia | Quantidade permitida de consultas |
| Data | Data do cadastro |

O banco de dados SQLite será utilizado para armazenar os registros do sistema.

## 📚 Conhecimentos aplicados

Durante o desenvolvimento foram utilizados:

- Variáveis e tipos de dados.
- Estruturas condicionais (`if`, `elif`, `else`).
- Estruturas de repetição (`while` e `for`).
- Funções (`def` e `return`).
- Listas e dicionários.
- Tratamento de exceções (`try` e `except`).
- Manipulação de strings (`strip`, `replace`, `isalpha`).
- Comandos SQL (`CREATE TABLE`, `INSERT`, `SELECT` e `UPDATE`).
- Integração entre Python e SQLite.
- Consultas parametrizadas e persistência de dados.

## 🎯 Objetivo

Desenvolver conhecimentos práticos em programação Python e banco de dados relacionais, aplicando conceitos de desenvolvimento de sistemas em um cenário relacionado ao faturamento hospitalar.

## 👨‍💻 Autor

Projeto desenvolvido para fins de aprendizado e evolução na área de desenvolvimento de software.
