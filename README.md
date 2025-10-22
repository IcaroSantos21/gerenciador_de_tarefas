# 📋 Sistema de Gerenciamento de Tarefas (To-Do List)

Este é um projeto prático desenvolvido em Python para gerenciar tarefas utilizando um banco de dados **MySQL** como persistência de dados. O objetivo é demonstrar proficiência na integração de Python com SQL, abrangendo as operações fundamentais de **CRUD (Create, Read, Update, Delete)**.

**Habilidades Demonstradas:**
* **Python Básico:** Funções, estruturas de controle de fluxo, tratamento de entrada de usuário.
* **SQL Básico:** Criação de tabelas, inserção, seleção, atualização e exclusão de dados.
* **Conexão de Banco de Dados:** Uso do conector oficial do MySQL em Python (`mysql-connector-python`).

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Banco de Dados:** MySQL
* **Biblioteca Python:** `mysql-connector-python`

---

## 🛠️ Instalação e Configuração

Siga os passos abaixo para rodar o projeto em sua máquina.

### 1. Pré-requisitos

Certifique-se de que você tem o MySQL Server instalado e em execução.

### 2. Configuração do Ambiente Python

Crie um ambiente virtual e instale a dependência necessária:

```bash
# Crie o ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Linux/macOS
# ou venv\Scripts\activate.bat no Windows

# Instale o conector MySQL
pip install mysql-connector-python