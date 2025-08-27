class Tarefa:
    def __init__(self, titulo:str, descricao:str, data:str, status:str, id_:int=None):
        self.id = id_
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        # Se status for None, assumimos que o banco vai usar o default "PENDENTE"
        self.status = status if status is not None else "Pendente"

    def __repr__(self):
        return f"<Tarefa {self.id if self.id else 'Sem ID'} - {self.titulo}>"
    
