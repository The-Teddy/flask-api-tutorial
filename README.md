# Flask API Tutorial 🚀

Este repositório contém o código de um tutorial passo a passo para construir uma API com Flask.

# 📌 O que você aprenderá?

✅ Criar e ativar um ambiente virtual Python
✅ Instalar Flask, Flask-CORS e dotenv
✅ Criar um projeto organizado com controllers, services e models
✅ Modularizar rotas usando Blueprint
✅ Criar e utilizar variáveis de ambiente
✅ Implementar CORS corretamente
✅ Criar um CRUD básico (sem banco de dados)
✅ Testar os endpoints com Postman

# 🔥 Branches Disponíveis

Cada branch contém um estágio do tutorial:

Branch | Conteúdo

v1-basic-api | API inicial com Flask, CORS e Postman

# Para visualizar uma versão específica, use:

git checkout branch_name

# 🛠 Como configurar o projeto

# Clone o repositório

git clone https://github.com/seu-usuario/flask-api-tutorial.git
cd flask-api-tutorial

# Crie e ative o ambiente virtual

python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

# Instale as dependências

pip install -r requirements.txt

# Renomeie e configure as variáveis de ambiente

cp .env.example .env

# Rode a API

flask run

# 📌 Testando a API

Acesse no navegador ou Postman:

http://127.0.0.1:5000/

Para acessar o endpoint de usuários:

http://127.0.0.1:5000/users
