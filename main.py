from fastapi import FastAPI
# Importamos el router desde el archivo controllers.py
from controllers import router as task_router

app = FastAPI(
    title="TaskFlow API",
    description="API de Estructuras de Datos (Lista, Pila, Cola)",
    version="1.0.0"
)

# Incluimos las rutas de los controladores
app.include_router(task_router)

@app.get("/")
def home():
    return {
        "message": "TaskFlow API funcionando",
        "docs": "Ve a /docs para probar los endpoints"
    }