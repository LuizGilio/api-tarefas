from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import banco
import psycopg2

app = FastAPI()

class Tarefa(BaseModel):
    titulo: str

@app.on_event("startup")
def startup():
    banco.criar_tabela()

@app.get("/tarefas")
def listar_tarefas():
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, titulo, concluida FROM tarefas")
    resultado = cursor.fetchall()
    conexao.close()
    tarefas = []
    for row in resultado:
        tarefas.append({
            "id": row[0],
            "titulo": row[1],
            "concluida": row[2]
        })
    return tarefas

@app.post("/tarefas")
def adicionar_tarefa(tarefa: Tarefa):
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO tarefas (titulo) VALUES (%s) RETURNING id",
        (tarefa.titulo,)
    )
    id_novo = cursor.fetchone()[0]
    conexao.commit()
    conexao.close()
    return {"id": id_novo, "titulo": tarefa.titulo, "concluida": False}

@app.put("/tarefas/{id}")
def concluir_tarefa(id: int):
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE tarefas SET concluida = TRUE WHERE id = %s",
        (id,)
    )
    if cursor.rowcount == 0:
        conexao.close()
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    conexao.commit()
    conexao.close()
    return {"mensagem": "Tarefa concluída"}

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "DELETE FROM tarefas WHERE id = %s",
        (id,)
    )
    if cursor.rowcount == 0:
        conexao.close()
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    conexao.commit()
    conexao.close()
    return {"mensagem": "Tarefa deletada"}