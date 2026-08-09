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

app = FastAPI(
    title="Sublima Decryptor API",
    description="Análise forense digital — OCR + Visão",
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
        "docs": "/docs",
        "slogan": "A Luz que Revela o que está Oculto",
        "vision_configured": vision_configured(),
    }
