"""Motor de análise de imagem — v0.2.2-ocr (técnico + OCR + visão opcional)"""
from __future__ import annotations

import asyncio
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Optional

from PIL import Image, ExifTags
from app.services.vision import analyze_with_vision, vision_configured
from app.services.ocr import extract_text, ocr_available


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


def _merge_vision(layers: dict, vision: Optional[dict]) -> dict:
    if not vision or vision.get("_error"):
        if vision and vision.get("_error"):
            layers["symbolic"]["status"] = "vision_error"
            layers["symbolic"]["summary"] = f"Falha no modelo de visão: {vision['_error']}"
        return layers
    if vision.get("literal_summary"):
        layers["literal"]["summary"] = vision["literal_summary"]
        layers["literal"]["source"] = "vision+technical"
    layers["symbolic"] = {
        "title": "Camada simbólica", "status": "ok",
        "summary": vision.get("symbolic") or "Elementos detectados pelo modelo de visão.",
        "elements": vision.get("elements") or [], "source": "vision_model",
    }
    layers["geopolitical"] = {
        "title": "Camada geopolítica / narrativa",
        "status": "ok" if vision.get("geopolitical") else "empty",
        "summary": vision.get("geopolitical") or "Sem leitura geopolítica evidente.",
        "source": "vision_model",
    }
    layers["memetic"] = {
        "title": "Camada memética",
        "status": "ok" if vision.get("memetic") else "empty",
        "summary": vision.get("memetic") or "Sem referência memética evidente.",
        "source": "vision_model",
    }
    layers["hypotheses"] = {
        "title": "Hipóteses / easter eggs",
        "items": vision.get("hypotheses") or [],
        "note": "Hipóteses com nível de confiança — não são fatos.",
        "source": "vision_model",
    }
    return layers


def analyze_image(path: str, original_name: str = "", use_vision: bool = True) -> dict[str, Any]:
    p = Path(path)
    img = Image.open(p)
    width, height = img.size
    mode = img.mode
    fmt = img.format or p.suffix.lstrip(".").upper()
    exif = _exif_dict(img)
    colors = _color_summary(img)
    density = "alta" if width * height > 1_000_000 else ("média" if width * height > 300_000 else "baixa")
    now = datetime.now(timezone.utc).isoformat()
    technical_ctx = {"format": fmt, "width": width, "height": height, "has_exif": bool(exif), "dominant_colors": colors[:3]}

    layers = {
        "literal": {
            "title": "Camada literal",
            "summary": f"Imagem {fmt} {width}×{height}px, modo {mode}. Densidade visual {density}.",
            "facts": [
                f"Dimensões: {width} × {height}", f"Formato: {fmt}",
                f"Arquivo: {original_name or p.name}", f"Tamanho: {p.stat().st_size} bytes",
            ],
            "source": "technical",
        },
        "symbolic": {"title": "Camada simbólica", "status": "pending_vision_model",
                      "summary": "Configure XAI_API_KEY ou OPENAI_API_KEY.", "elements": []},
        "geopolitical": {"title": "Camada geopolítica / narrativa", "status": "pending_vision_model",
                         "summary": "Disponível após inventário simbólico."},
        "memetic": {"title": "Camada memética", "status": "pending_vision_model",
                    "summary": "Disponível após inventário simbólico."},
        "hypotheses": {"title": "Hipóteses / easter eggs", "items": [],
                       "note": "Somente após evidência visual."},
    }

    vision_result = None
    vision_status = "not_configured"
    if use_vision and vision_configured():
        try:
            try:
                vision_result = asyncio.get_event_loop().run_until_complete(
                    analyze_with_vision(str(p), technical_ctx))
            except RuntimeError:
                vision_result = asyncio.run(analyze_with_vision(str(p), technical_ctx))
        except Exception as e:
            vision_result = {"_error": str(e)}
        if vision_result and not vision_result.get("_error"):
            vision_status = "ok"
            layers = _merge_vision(layers, vision_result)
        elif vision_result and vision_result.get("_error"):
            vision_status = "error"
            layers = _merge_vision(layers, vision_result)
        else:
            vision_status = "empty_response"

    ocr_result = extract_text(str(p))
    if ocr_result.get("text"):
        layers["literal"]["facts"].append(f"OCR: {ocr_result['word_count']} palavras extraídas")
        if ocr_result.get("possible_microtext"):
            layers["literal"]["facts"].append("Possível microtexto detectado")
        layers["ocr"] = {
            "title": "OCR / Texto extraído", "status": "ok",
            "text": ocr_result["text"][:3000],
            "word_count": ocr_result["word_count"],
            "char_count": ocr_result["char_count"],
            "confidence_avg": ocr_result.get("confidence_avg"),
            "possible_microtext": ocr_result.get("possible_microtext", False),
            "engine": ocr_result.get("engine"),
        }
    else:
        layers["ocr"] = {
            "title": "OCR / Texto extraído",
            "status": "empty" if ocr_result.get("available") else "unavailable",
            "text": "", "error": ocr_result.get("error"),
            "available": ocr_result.get("available"),
        }

    report = {
        "meta": {
            "service": "Sublima Decryptor", "version": "0.2.2-ocr",
            "analyzed_at": now, "original_filename": original_name or p.name,
            "format": fmt, "dimensions": {"width": width, "height": height},
            "mode": mode, "file_size_bytes": p.stat().st_size,
            "visual_density": density, "vision_status": vision_status,
            "vision_configured": vision_configured(),
            "ocr_available": ocr_available(),
        },
        "technical": {
            "exif": exif, "dominant_colors": colors, "has_exif": bool(exif),
            "ocr_word_count": ocr_result.get("word_count", 0),
        },
        "layers": layers,
        "disclaimer": (
            "Interpretações além da camada literal são hipóteses analíticas. "
            "Não constituem prova de intenção do autor nem de conspiração."
        ),
        "next_steps": [
            "Configure XAI_API_KEY ou OPENAI_API_KEY para camadas simbólicas.",
            "Esteganografia (LSB/DCT) planejada para Fase 3.",
        ],
        "prompt_hint": {"system_prompt_path": "prompts/SYSTEM_PROMPT.md"},
    }
    if vision_result and vision_result.get("_provider"):
        report["meta"]["vision_provider"] = vision_result["_provider"]
    return report
