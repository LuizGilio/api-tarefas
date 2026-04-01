import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conexao = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas(
        id SERIAL PRIMARY KEY,
        titulo TEXT NOT NULL,
        concluida BOOLEAN DEFAULT FALSE
        )   
    """) 

    conexao.commit()
    conexao.close()   