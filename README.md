# API de Tarefas

API REST construída com FastAPI e PostgreSQL para gerenciamento de tarefas.

## API em produção

Acesse a documentação interativa:
https://web-production-4d5e5.up.railway.app/docs


## Tecnologias

- Python 3.14
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn

## Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /tarefas | Lista todas as tarefas |
| POST | /tarefas | Adiciona uma tarefa |
| PUT | /tarefas/{id} | Conclui uma tarefa |
| DELETE | /tarefas/{id} | Deleta uma tarefa |

## Como rodar

Clone o repositório:
```bash
git clone https://github.com/LuizGilio/api-tarefas.git
```

Entre na pasta:
```bash
cd api-tarefas
```

Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Configure o PostgreSQL e crie o banco:
```bash
sudo service postgresql start
sudo -u postgres psql -c "CREATE USER luizotavio WITH PASSWORD 'senha123';"
sudo -u postgres psql -c "CREATE DATABASE tarefas_db OWNER luizotavio;"
```

Rode o servidor:
```bash
uvicorn main:app --reload
```

Acesse a documentação em:
```
http://localhost:8000/docs
```

## Aprendizados

- API REST com FastAPI
- Rotas GET, POST, PUT, DELETE
- Integração Python + PostgreSQL
- Validação de dados com Pydantic
- Documentação automática com Swagger UI