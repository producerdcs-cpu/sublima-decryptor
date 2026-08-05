from fastapi import APIRouter
from app.services.vision import vision_configured

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Sublima Decryptor API",
        "phase": "1.1",
        "version": "0.2.1-fase1.1",
        "vision_configured": vision_configured(),
    }
