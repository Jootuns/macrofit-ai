from fastapi import FastAPI


from backend.app.api.auth import router as auth_router
from backend.app.api.health import router as health_router

app = FastAPI(
    title="MacroFit AI API",
    description="API para la aplicación de nutrición y entrenamiento MacroFit AI.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la API de MacroFit AI",
        "status": "running",
    }


app.include_router(health_router)
app.include_router(auth_router)