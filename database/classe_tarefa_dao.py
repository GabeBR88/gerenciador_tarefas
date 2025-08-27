import mysql.connector
import os
from dotenv import load_dotenv
from models.classe_tarefa import Tarefa

load_dotenv()

class TarefaDAO:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

    
    def create_connection(self):
        return mysql.connector.connect(
            host= self.host,
            user= self.user,
            password= self.password,
            database= self.database
        )
    

    def criar(self, tarefa:Tarefa):
        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO tarefas_list (titulo, descricao, data_tarefa, staus_tarefa) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (tarefa.titulo, tarefa.descricao, tarefa.data, tarefa.status))
        conn.commit()
        conn.close()

    
    def listar(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas_list")
        linhas = cursor.fetchall()
        conn.close()
        return [Tarefa(*linha) for linha in linhas]
    

    def atualizar(self, tarefa: Tarefa):
        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "UPDATE tarefas_list SET titulo=%s, descricao=%s, data=%s, status=%s WHERE id=%s"
        cursor.execute(sql, (tarefa.titulo, tarefa.descricao, tarefa.data, tarefa.status, tarefa.id))
        conn.commit()
        conn.close()
        
    
    def deletar(self, id_: int):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas_list WHERE id=%s", (id_,))
        conn.commit()
        conn.close()