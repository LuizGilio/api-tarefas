import psycopg2

def conectar():
    conexao = psycopg2.connect(
        host="localhost",
        database="tarefas_db",
        user="luizotavio",
        password="senha123"
    )
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