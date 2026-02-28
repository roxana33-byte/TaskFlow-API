from models import Task, Action
from repository import TaskRepository
from typing import List, Optional

class TaskFlowService:
    def __init__(self, repository: TaskRepository):
        self.repo = repository

    # Lógica de Backlog (Lista Enlazada) 
    def create_task(self, title: str) -> Task:
        new_task = Task(title=title)
        self.repo.save_task(new_task)
        # Registro automático en la pila de Undo
        self.repo.push_action(Action(description=f"Tarea creada: {title}"))
        return new_task

    def get_backlog(self) -> List[Task]:
        return self.repo.get_all_tasks()

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        return self.repo.find_task_by_id(task_id)

    def delete_task(self, task_id: str) -> bool:
        task = self.repo.find_task_by_id(task_id)
        if task:
            self.repo.delete_task(task_id)
            self.repo.push_action(Action(description=f"Tarea eliminada: {task.title}"))
            return True
        return False

    #Lógica de Undo (Pila / Stack)
    def get_last_action(self) -> Optional[Action]:
        return self.repo.peek_action()

    def undo_last_action(self) -> Optional[Action]:
        # Pop de la pila
        return self.repo.pop_action()

    # Lógica de Queue (Cola) 
    def add_to_queue(self, task_id: str) -> Optional[Task]:
        task = self.repo.find_task_by_id(task_id)
        if task:
            self.repo.enqueue_task(task)
            return task
        return None

    def get_next_in_queue(self) -> Optional[Task]:
        return self.repo.peek_queue()

    def process_next_task(self) -> Optional[Task]:
        # Dequeue de la cola
        return self.repo.dequeue_task()