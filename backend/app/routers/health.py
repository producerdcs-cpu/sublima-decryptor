from fastapi import APIRouter
from app.services.vision import vision_configured
from app.services.ocr import ocr_available

router = APIRouter()

APP_VERSION = "0.3.0"


@router.get("/health")
def health():
    ocr = ocr_available()
    vision = vision_configured()
    # ok se API sobe; degraded se OCR ausente (comum em dev sem tesseract)
    status = "ok" if ocr else "degraded"
    return {
        "status": status,
        "service": "Sublima Decryptor API",
        "phase": "v0.3-stable",
        "version": APP_VERSION,
        "brand": "© DcsProducer®",
        "vision_configured": vision,
        "ocr_available": ocr,
        "stego_lsb": True,
        "capabilities": {
            "technical": True,
            "ocr": ocr,
            "vision": vision,
            "steganography_lsb": True,
        },
    }
