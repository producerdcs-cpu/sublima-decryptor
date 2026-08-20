import uuid
from pathlib import Path
from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.image_analyzer import analyze_image

router = APIRouter()

UPLOAD_DIR = Path(__file__).resolve().parent.parent.parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff", ".tif"}
MAX_BYTES = 15 * 1024 * 1024


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(400, "Arquivo sem nome")

    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED:
        raise HTTPException(400, f"Formato não suportado: {ext}. Use: {', '.join(sorted(ALLOWED))}")

    content = await file.read()
    if not content:
        raise HTTPException(400, "Arquivo vazio")
    if len(content) > MAX_BYTES:
        raise HTTPException(400, "Arquivo maior que 15MB")

    file_id = str(uuid.uuid4())
    save_path = UPLOAD_DIR / f"{file_id}{ext}"
    save_path.write_bytes(content)

    try:
        report = analyze_image(str(save_path), original_name=file.filename)
        report["file_id"] = file_id
        return report
    except Exception as e:
        raise HTTPException(500, f"Erro na análise: {str(e)}") from e
    finally:
        # mantém arquivo curto prazo para debug; em produção futura limpar
        pass
