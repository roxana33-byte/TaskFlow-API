#(capa de Modelo) se define la forma de los datos;
#pydantic para validación
from pydantic import BaseModel, Field
#uuid para generar IDs únicos
from uuid import uuid4, UUID
#datetime para la fecha de creación
from datetime import datetime
from typing import Optional

# Modelo para la Tarea (Task)
class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    createdAt: datetime = Field(default_factory=datetime.now)

# Modelo para las acciones del Undo (Pila)
class Action(BaseModel):
    description: str
    timestamp: datetime = Field(default_factory=datetime.now)

# Modelo para recibir datos del cliente (solo el título)
class TaskCreate(BaseModel):
    title: str