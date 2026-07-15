from fastapi import FastAPI

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


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }