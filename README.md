# 🛠️ Agendaro – Backend

Este repositório apresenta a API do sistema **Agendaro**, desenvolvida com **Python** e **Django REST Framework**, responsável por gerenciar os dados e regras de negócio do projeto.

Este repositório está disponível **exclusivamente para fins de demonstração profissional**, com o objetivo de apresentar minhas habilidades em desenvolvimento backend para **entrevistadores, analistas e recrutadores**.

## 📌 Propósito do Repositório

O backend do Agendaro é uma **API RESTful** que fornece os dados e serviços necessários para o funcionamento do frontend. O objetivo deste repositório é demonstrar:

- Estruturação de projetos em Django
- Desenvolvimento de APIs REST com boas práticas
- Organização modular e escalável
- Experiência com autenticação, permissões e rotas protegidas

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Django**
- **Django REST Framework**
- **SQLite3** (em desenvolvimento) / PostgreSQL (em produção)
- **Django CORS Headers**
- **Autenticação JWT**

## 🧠 Técnicas Demonstradas

- Criação de API REST com Django REST Framework
- Estrutura de models, serializers, views e rotas
- Token JWT com autenticação customizada
- Versionamento e organização modular da API
- Utilização de permissões e filtros
- Integração com frontend (Angular)

## 📁 Estrutura do Projeto

```
agendarobackpublic/
├── agendaro/ # Aplicação principal
├── apps
|   ├── business
|   ├── client
├── manage.py
├── requirements.txt
├── db.sqlite3
└── envAgendaro # Virtual Environment

```


## 🔐 Endpoints Principais

- `/auth/login/` – Login com JWT
- `/auth/register/`- Register User com JWT
- `/business/` – Gerenciamento de empresas
- `/client/` – Gerenciamento de Clientes
- (entre outros...)

> Autenticação via JWT protegendo rotas sensíveis.

## ▶️ Como Executar Localmente

```bash
# Clone o projeto
git clone https://github.com/seuusuario/agendaro-backend.git
cd agendaro-backend

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
