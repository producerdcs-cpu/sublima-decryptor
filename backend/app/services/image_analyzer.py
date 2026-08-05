"""Motor de análise de imagem — MVP"""
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image, ExifTags


def _exif_dict(img: Image.Image) -> dict:
    data = {}
    try:
        raw = img.getexif()
        if not raw:
            return data
        for tag_id, value in raw.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            try:
                data[str(tag)] = str(value)[:200]
            except Exception:
                pass
    except Exception:
        pass
    return data


def _color_summary(img: Image.Image) -> list:
    small = img.convert("RGB").resize((50, 50))
    colors = small.getcolors(2500) or []
    colors = sorted(colors, key=lambda x: x[0], reverse=True)[:5]
    return [{"rgb": list(rgb), "weight": round(count / 2500, 3)} for count, rgb in colors]


def analyze_image(path: str, original_name: str = "") -> dict:
    p = Path(path)
    img = Image.open(p)
    width, height = img.size
    mode = img.mode
    fmt = img.format or p.suffix.lstrip(".").upper()
    exif = _exif_dict(img)
    colors = _color_summary(img)
    density = "alta" if width * height > 1_000_000 else ("média" if width * height > 300_000 else "baixa")
    now = datetime.now(timezone.utc).isoformat()

    return {
        "meta": {
            "service": "Sublima Decryptor",
            "version": "0.2.0-mvp",
            "analyzed_at": now,
            "original_filename": original_name or p.name,
            "format": fmt,
            "dimensions": {"width": width, "height": height},
            "mode": mode,
            "file_size_bytes": p.stat().st_size,
            "visual_density": density,
        },
        "technical": {
            "exif": exif,
            "dominant_colors": colors,
            "has_exif": bool(exif),
            "notes": [
                "Metadados EXIF extraídos quando presentes.",
                "Cores dominantes por quantização local (MVP).",
                "Detectores de esteganografia (LSB/DCT) entram na Fase 3.",
            ],
        },
        "layers": {
            "literal": {
                "title": "Camada literal",
                "summary": f"Imagem {fmt} {width}×{height}px, modo {mode}. Densidade visual {density}.",
                "facts": [
                    f"Dimensões: {width} × {height}",
                    f"Formato: {fmt}",
                    f"Arquivo: {original_name or p.name}",
                    f"Tamanho: {p.stat().st_size} bytes",
                ],
            },
            "symbolic": {
                "title": "Camada simbólica",
                "status": "pending_vision_model",
                "summary": "Estrutura pronta. Conecte modelo de visão + LLM (prompts/SYSTEM_PROMPT.md) na Fase 1.1.",
                "elements": [],
            },
            "geopolitical": {
                "title": "Camada geopolítica / narrativa",
                "status": "pending_vision_model",
                "summary": "Disponível após inventário simbólico.",
            },
            "memetic": {
                "title": "Camada memética",
                "status": "pending_vision_model",
                "summary": "Disponível após inventário simbólico.",
            },
            "hypotheses": {
                "title": "Hipóteses / easter eggs",
                "items": [],
                "note": "Somente após evidência visual e com nível de confiança.",
            },
        },
        "disclaimer": (
            "Interpretações além da camada literal são hipóteses analíticas. "
            "Não constituem prova de intenção do autor nem de conspiração. "
            "O Sublima Decryptor não afirma verdades ocultas; oferece ferramentas para leitura crítica."
        ),
        "next_steps": [
            "Conectar modelo de visão (Fase 1.1) para inventário de objetos.",
            "Rodar OCR para texto e microtexto.",
            "Aplicar detectores de esteganografia (Fase 3).",
        ],
        "prompt_hint": {
            "system_prompt_path": "prompts/SYSTEM_PROMPT.md",
            "usage": "Envie a imagem + este relatório técnico ao LLM com o system prompt do Motor de Decodificação.",
        },
    }
