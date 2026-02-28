# TaskFlow-API
TaskFlow API - Estructuras de Datos Lineales
Este proyecto es una API REST construida con Python y FastAPI que modela operaciones típicas de un sistema de tareas utilizando tres estructuras de datos fundamentales: Lista Enlazada, Pila y Cola.

Stack y Librerías Utilizadas
Python 3.10+: Lenguaje base del proyecto.

FastAPI: Framework moderno para la creación de la API y documentación automática con Swagger.

Uvicorn: Servidor para ejecutar la aplicación.

Pydantic: Utilizado en models.py para la validación de datos y definición de esquemas.

UUID: Para generar identificadores únicos para cada tarea.

Collections (deque): Implementada en repository.py para gestionar la Cola de procesamiento de forma eficiente.

Arquitectura por Capas
El proyecto respeta la separación de responsabilidades:

Model (models.py): Define la estructura de Task y Action.

Repository (repository.py): Gestiona el almacenamiento en memoria. Aquí residen la Lista (Backlog), la Pila (Undo) y la Cola (Queue).

Service (services.py): Contiene la lógica de negocio (ej. registrar un "Undo" automáticamente al crear una tarea).

Controller (controllers.py / main.py): Gestiona las peticiones HTTP y las respuestas.

Funcionalidades y Estructuras
Lista Enlazada (Backlog): Permite crear, listar y eliminar tareas con un orden dinámico.

Pila / Stack (Undo): Sistema LIFO (Last-In, First-Out) que registra las acciones realizadas para poder visualizarlas o "deshacerlas".

Cola / Queue (Processing): Sistema FIFO (First-In, First-Out) para encolar tareas y procesarlas en orden de llegada.

Cómo ejecutar
Asegúrate de tener instalado Python.

Instala las dependencias: pip install fastapi uvicorn.

Ejecuta el servidor: python -m uvicorn main:app --reload.

Prueba la API en: http://127.0.0.1:8000/docs
