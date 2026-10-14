import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.users import router as users_router

logger = logging.getLogger(__name__)

app = FastAPI(
    title="MacroFit AI API",
    description="API para la aplicación de nutrición y entrenamiento MacroFit AI.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error inesperado: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"},
    )


@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la API de MacroFit AI",
        "status": "running",
    }


app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)
