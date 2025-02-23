# 📌 API de Cardápio - FastAPI + PostgreSQL + Docker

## 📖 Sobre o Projeto

Este projeto é uma API REST para gerenciamento de um **cardápio**, desenvolvida com **FastAPI** e banco de dados **PostgreSQL**, totalmente conteinerizada usando **Docker**.

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI** (Framework leve e performático para APIs)
- **PostgreSQL** (Banco de dados relacional)
- **SQLAlchemy** (ORM para manipulação do banco)
- **Alembic** (Migrations)
- **Docker & Docker Compose** (Gerenciamento de containers)
- **Uvicorn** (Servidor ASGI para rodar a API)
- **pytest + httpx** (Testes automatizados)

## 📂 Estrutura do Projeto

```
/cardapio-api
│── /app
│   │── /models         # Definição das tabelas do 
│   │── /schemas        # Schemas do Pydantic para 
│   │── /routes         # Rotas da API
│   │── /services       # Lógica de negócio
│   │── /db             # Configuração do banco e 
│   │── main.py         # Ponto de entrada da API
│── /tests              # Testes automatizados
│── .env                # Variáveis de ambiente
│── Dockerfile          # Arquivo para criar 
│── docker-compose.yml  # Orquestração dos 
│── requirements.txt    # Dependências do projeto
```

## 🛠️ Configuração e Execução

### 🔹 1. Pré-requisitos

Certifique-se de ter **Docker** e **Docker Compose** instalados:

```bash
docker --version
docker-compose --version
```

### 🔹 2. Clonar o Repositório

```bash
git clone https://github.com/seu-repositorio/cardapio-api.git
cd cardapio-api
```

### 🔹 3. Configurar Variáveis de Ambiente

Crie um arquivo **.env** na raiz do projeto e adicione:

```ini
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
POSTGRES_DB=cardapio
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 🔹 4. Construir e Subir os Containers

```bash
docker-compose up --build
```

A API estará disponível em **[http://localhost:8000](http://localhost:8000)**

### 🔹 5. Testar a API

Acesse a documentação interativa do FastAPI:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### 🔹 6. Verificar o Banco de Dados

Acesse o banco dentro do container:

```bash
docker exec -it cardapio_db psql -U admin -d cardapio
```

E rode:

```sql
\dt  -- Lista as tabelas
SELECT * FROM menu;  -- Verifica os dados cadastrados
```

## 📌 Funcionalidades

✅ Listagem de itens do cardápio (`GET /menu`)
✅ Criação de novos itens (`POST /menu`)
✅ Atualização de itens (`PUT /menu/{id}`)
✅ Remoção de itens (`DELETE /menu/{id}`)
✅ Persistência no PostgreSQL
✅ Testes automatizados

## 🚀 Próximos Passos

🔹 Melhorar autenticação com **JWT**
🔹 Implementar **paginação** nos endpoints
🔹 Criar **testes automatizados** mais robustos

---

**Desenvolvido por Roney Fernandes 💻🚀**

📱 Contato: 98981767685
