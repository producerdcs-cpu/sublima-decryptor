"""OCR — extração de texto e microtexto (Fase 1.2)"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from PIL import Image


def ocr_available() -> bool:
    try:
        import pytesseract
        pytesseract.get_tesseract_version()
        return True
    except Exception:
        return False


def extract_text(path: str, lang: str = "por+eng") -> dict[str, Any]:
    result: dict[str, Any] = {
        "engine": "tesseract",
        "available": ocr_available(),
        "text": "",
        "lines": [],
        "confidence_avg": None,
        "char_count": 0,
        "word_count": 0,
    }
    if not result["available"]:
        result["error"] = "Tesseract/pytesseract não disponível"
        return result
    try:
        import pytesseract
        img = Image.open(path)
        w, h = img.size
        if max(w, h) < 800:
            scale = max(2, int(1000 / max(w, h)))
            img = img.resize((w * scale, h * scale), Image.Resampling.LANCZOS)
        try:
            text = pytesseract.image_to_string(img, lang=lang)
        except Exception:
            text = pytesseract.image_to_string(img, lang="eng")
        text = (text or "").strip()
        result["text"] = text
        result["char_count"] = len(text)
        result["word_count"] = len(text.split()) if text else 0
        try:
            data = pytesseract.image_to_data(img, lang=lang, output_type=pytesseract.Output.DICT)
        except Exception:
            data = pytesseract.image_to_data(img, lang="eng", output_type=pytesseract.Output.DICT)
        lines, confs = [], []
        for i in range(len(data.get("text", []))):
            word = (data["text"][i] or "").strip()
            if not word:
                continue
            conf = float(data["conf"][i]) if data["conf"][i] != "-1" else None
            if conf is not None and conf >= 0:
                confs.append(conf)
            lines.append({
                "text": word, "confidence": conf,
                "left": data["left"][i], "top": data["top"][i],
                "width": data["width"][i], "height": data["height"][i],
            })
        result["lines"] = lines[:200]
        if confs:
            result["confidence_avg"] = round(sum(confs) / len(confs), 1)
        small = [L for L in lines if L.get("height") and L["height"] < 12]
        result["possible_microtext"] = len(small) >= 3
        result["small_word_count"] = len(small)
    except Exception as e:
        result["error"] = str(e)
    return result
