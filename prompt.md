📌 Contexto do Projeto
Estou desenvolvendo uma API REST para um cardápio utilizando Python (FastAPI) e um banco de dados PostgreSQL containerizado com Docker. O projeto segue boas práticas de desenvolvimento, incluindo uso de ORM (SQLAlchemy), versionamento do banco com Alembic, testes automatizados com pytest, e gerenciamento de dependências com Poetry ou pip.

📁 Estrutura do Projeto
O projeto está organizado da seguinte forma:


/delivery-api
│── /app
│   │── /models         # Definição das tabelas do banco
│   │── /schemas        # Schemas do Pydantic para validação
│   │── /routes         # Rotas da API
│   │── /services       # Lógica de negócio
│   │── /db             # Configuração do banco e migrations
│   │── main.py         # Ponto de entrada da API
│── /tests              # Testes automatizados
│── .env                # Variáveis de ambiente
│── Dockerfile          # Arquivo para criar imagem Docker
│── docker-compose.yml  # Orquestração dos containers
│── requirements.txt    # Dependências do projeto




🚀 Tecnologias Utilizadas
Linguagem: Python 3.10+
Framework: FastAPI (alternativa leve ao Flask, com tipagem e validação via Pydantic)
Banco de Dados: PostgreSQL (gerenciado via Docker)
ORM: SQLAlchemy (para manipulação do banco de dados)
Migrations: Alembic (para versionamento e controle das alterações no banco)
Gerenciamento de Dependências: Poetry ou pip
Testes Automatizados: pytest e httpx
Servidor de Produção: Gunicorn/Uvicorn
Autenticação: Planejo implementar autenticação via OAuth2 ou JWT futuramente
Conteinerização: Docker & Docker Compose (para orquestração dos serviços)


📌 O que já foi feito
✅ Criação do main.py, onde inicializamos o FastAPI e incluímos o roteamento.
✅ Definição da estrutura de pastas, seguindo um modelo escalável e modular.
✅ Configuração inicial do Dockerfile e docker-compose, garantindo que a API e o banco rodem dentro de containers.
✅ Instalação das dependências principais:

fastapi, uvicorn para rodar a API
sqlalchemy, psycopg2 para o banco
alembic para migrations
pytest, httpx para testes


📌 O que falta implementar?
🔹 Modelagem do banco de dados com SQLAlchemy: criar tabelas para os itens do cardápio.
🔹 Criação das rotas CRUD (GET, POST, PUT, DELETE) para gerenciar os itens do cardápio.
🔹 Conexão da API com o PostgreSQL via SQLAlchemy.
🔹 Migrations com Alembic, para versionar o banco de dados.
🔹 Testes automatizados para validar as funcionalidades.
🔹 Melhorias na segurança, como proteção contra SQL Injection e autenticação JWT.

📌 Próximos Passos
1️⃣ Criar os modelos de banco no diretório /models.
2️⃣ Implementar as rotas CRUD no diretório /routes.
3️⃣ Configurar o banco de dados no /db e conectar via SQLAlchemy.
4️⃣ Criar os schemas de validação com Pydantic no /schemas.
5️⃣ Configurar Alembic para gerenciar migrations.
6️⃣ Criar testes automatizados com pytest e httpx.