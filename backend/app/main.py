"""
Sublima Decryptor API — MVP
Upload de imagem → relatório forense em camadas
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import analyze, health

app = FastAPI(
    title="Sublima Decryptor API",
    description="Análise forense digital e decodificação subliminar — MVP",
    version="0.2.0-mvp",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(analyze.router, prefix="/api", tags=["analyze"])


@app.get("/")
def root():
    return {
        "service": "Sublima Decryptor",
        "version": "0.2.0-mvp",
        "docs": "/docs",
        "slogan": "A Luz que Revela o que está Oculto",
    }
