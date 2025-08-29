class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        if task:
            self.tasks.append(task)
            return "Tarefa adicionada"
        return "Tarefa inválida"
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return "Tarefa removida"
        return "Tarefa não encontrada"
    
    def list_tasks(self):
        return self.tasks if self.tasks else "Nenhuma tarefa cadastrada"
