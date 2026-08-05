from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Sublima Decryptor API",
        "phase": "MVP",
        "version": "0.2.0-mvp",
    }
