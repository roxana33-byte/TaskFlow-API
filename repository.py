#Aquí es donde vive la estructura de datos en memoria
#collections.deque es fundamental,es librería de Python diseñada para crear Colas (Queues) de forma eficiente
from collections import deque
from typing import List, Optional
from models import Task, Action

class TaskRepository:
    def __init__(self):
        # 1. Lista Enlazada (Backlog) - Usamos una lista de Python
        self._backlog: List[Task] = []
        
        # 2. Pila / Stack (Undo) - LIFO (Last In, First Out)
        self._undo_stack: List[Action] = []
        
        # 3. Cola / Queue (Processing) - FIFO (First In, First Out)
        self._processing_queue = deque()

    #  Operaciones de Backlog
    def save_task(self, task: Task):
        self._backlog.append(task)
        return task

    def get_all_tasks(self):
        return self._backlog

    def find_task_by_id(self, task_id: str):
        return next((t for t in self._backlog if t.id == task_id), None)

    def delete_task(self, task_id: str):
        self._backlog = [t for t in self._backlog if t.id != task_id]

    # Operaciones de Undo (Pila) 
    def push_action(self, action: Action):
        self._undo_stack.append(action)

    def pop_action(self):
        if not self._undo_stack:
            return None
        return self._undo_stack.pop()

    def peek_action(self):
        return self._undo_stack[-1] if self._undo_stack else None

    # Operaciones de Queue (Cola) 
    def enqueue_task(self, task: Task):
        self._processing_queue.append(task)

    def dequeue_task(self):
        if not self._processing_queue:
            return None
        return self._processing_queue.popleft() # Saca el primero que entró

    def peek_queue(self):
        return self._processing_queue[0] if self._processing_queue else None