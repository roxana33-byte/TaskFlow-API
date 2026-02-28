#es donde se recibe las peticiones de los usuarios
#fastapi para crear las rutas
from fastapi import APIRouter, HTTPException
#HTTPException para enviar errores
from models import TaskCreate
from services import TaskFlowService
from repository import TaskRepository

# Inicializamos el repositorio y el servicio (Singleton para la sesión actual)
repo = TaskRepository()
service = TaskFlowService(repo)

router = APIRouter()

#  BACKLOG (Lista Enlazada)

@router.post("/backlog/tasks", status_code=201)
def create_task(payload: TaskCreate):
    return service.create_task(payload.title)

@router.get("/backlog/tasks", status_code=200)
def list_tasks():
    return service.get_backlog()

@router.get("/backlog/tasks/{task_id}", status_code=200)
def get_task(task_id: str):
    task = service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

@router.delete("/backlog/tasks/{task_id}", status_code=204)
def delete_task(task_id: str):
    success = service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar: ID no existe")
    return None

# UNDO (Pila / Stack) 

@router.get("/undo/peek", status_code=200)
def peek_undo():
    action = service.get_last_action()
    if not action:
        raise HTTPException(status_code=404, detail="Historial de acciones vacío")
    return action

@router.delete("/undo", status_code=204)
def undo_action():
    action = service.undo_last_action()
    if not action:
        raise HTTPException(status_code=404, detail="Nada que deshacer")
    return None

# QUEUE (Cola / Processing)

@router.post("/queue", status_code=201)
def enqueue_task(task_id: str):
    task = service.add_to_queue(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada en el backlog")
    return {"message": "Tarea encolada correctamente", "task": task}

@router.get("/queue/next", status_code=200)
def view_next():
    task = service.get_next_in_queue()
    if not task:
        raise HTTPException(status_code=404, detail="La cola está vacía")
    return task

@router.delete("/queue", status_code=200)
def process_task():
    task = service.process_next_task()
    if not task:
        raise HTTPException(status_code=404, detail="No hay tareas para procesar")
    return {"message": "Tarea procesada", "task": task}