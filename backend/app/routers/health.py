from fastapi import APIRouter
from app.services.vision import vision_configured
from app.services.ocr import ocr_available

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Sublima Decryptor API",
        "phase": "1.2-ocr",
        "version": "0.2.2-ocr",
        "vision_configured": vision_configured(),
        "ocr_available": ocr_available(),
    }
