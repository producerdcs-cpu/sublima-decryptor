"""Sublima Decryptor API — v0.2.2-ocr"""
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import analyze, health
from app.services.vision import vision_configured
from app.services.ocr import ocr_available

app = FastAPI(
    title="Sublima Decryptor API",
    description="Análise forense digital — OCR + Visão + Esteganografia (em evolução)",
    version="0.2.2-ocr",
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
        "version": "0.2.2-ocr",
        "slogan": "A Luz que Revela o que está Oculto",
        "status": {
            "ocr_available": ocr_available(),
            "vision_configured": vision_configured(),
        },
        "links": {
            "docs": "/docs",
            "health": "/api/health",
            "analyze": "/api/analyze",
            "openapi": "/openapi.json",
        },
        "message": "Use /docs para interagir com a API (Swagger UI).",
    }
