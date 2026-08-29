"""Análise LSB (Least Significant Bit) — Fase 3.1 + extração básica de payload

- Planos de bit + entropia + score de suspeita
- Extração sequencial de bits LSB → tentativa de texto legível
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image


def _bit_plane(channel: np.ndarray, bit: int = 0) -> np.ndarray:
    """Retorna o plano do bit indicado (0 = LSB)."""
    return ((channel >> bit) & 1).astype(np.uint8)


def _bit_ratio(plane: np.ndarray) -> float:
    """Proporção de bits 1 no plano."""
    return float(np.mean(plane))


def _entropy(plane: np.ndarray) -> float:
    """Entropia de Shannon do plano de bits (0 ou 1)."""
    p = np.mean(plane)
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return float(-p * np.log2(p) - (1 - p) * np.log2(1 - p))


def _extract_lsb_bits(arr: np.ndarray, max_bits: int = 8 * 512) -> np.ndarray:
    """Extrai LSBs em ordem row-major, canal a canal (R,G,B)."""
    bits = []
    h, w, c = arr.shape
    count = 0
    for y in range(h):
        for x in range(w):
            for ch in range(c):
                bits.append(int(arr[y, x, ch]) & 1)
                count += 1
                if count >= max_bits:
                    return np.array(bits, dtype=np.uint8)
    return np.array(bits, dtype=np.uint8)


def _bits_to_bytes(bits: np.ndarray) -> bytes:
    """Agrupa bits em bytes (MSB-first dentro do byte)."""
    n = (len(bits) // 8) * 8
    if n == 0:
        return b""
    bits = bits[:n].reshape(-1, 8)
    values = np.packbits(bits, bitorder="big")
    return values.tobytes()


def _try_decode_text(raw: bytes) -> dict[str, Any]:
    """Tenta interpretar bytes como texto; retorna preview e avaliação."""
    if not raw:
        return {"payload_text": None, "payload_preview": None, "payload_encoding": None}

    # Corta em NULL se houver (comum em payloads simples)
    null_at = raw.find(b"\x00")
    candidate = raw[:null_at] if null_at > 0 else raw[:256]

    for enc in ("utf-8", "latin-1", "ascii"):
        try:
            text = candidate.decode(enc)
        except Exception:
            continue
        # Heurística: proporção de caracteres imprimíveis
        printable = sum(1 for ch in text if ch.isprintable() or ch in "\n\r\t")
        ratio = printable / max(len(text), 1)
        if ratio >= 0.75 and len(text.strip()) >= 4:
            preview = text[:200]
            return {
                "payload_text": text[:2000] if len(text) <= 2000 else text[:2000] + "…",
                "payload_preview": preview,
                "payload_encoding": enc,
                "payload_printable_ratio": round(ratio, 3),
            }

    # Fallback: hex preview
    hx = candidate[:64].hex()
    return {
        "payload_text": None,
        "payload_preview": hx + ("…" if len(candidate) > 64 else ""),
        "payload_encoding": "hex",
        "payload_printable_ratio": 0.0,
    }


def analyze_lsb(path: str | Path) -> dict[str, Any]:
    """Analisa LSBs e tenta extrair payload textual sequencial."""
    try:
        img = Image.open(path).convert("RGB")
        arr = np.array(img)
        h, w, _ = arr.shape

        channels_info = {}
        scores = []

        for i, name in enumerate(("R", "G", "B")):
            channel = arr[:, :, i]
            plane = _bit_plane(channel, bit=0)
            ratio = _bit_ratio(plane)
            ent = _entropy(plane)

            deviation = abs(ent - 0.95)
            channel_score = min(1.0, deviation * 4.0)

            channels_info[name] = {
                "bit_ratio": round(ratio, 4),
                "entropy": round(ent, 4),
                "score": round(channel_score, 3),
                "flag": "anomalous" if channel_score > 0.45 else "normal",
            }
            scores.append(channel_score)

        overall_score = float(np.mean(scores))

        if overall_score > 0.55:
            status = "suspicious"
            summary = "Padrão de bits menos significativos com desvio estatístico detectado."
        elif overall_score > 0.35:
            status = "suspicious"
            summary = "Leve anomalia nos LSBs — recomenda-se análise complementar."
        else:
            status = "clean"
            summary = "Nenhuma anomalia relevante detectada nos planos LSB."

        # Extração de payload (sempre tenta; útil mesmo em imagens "clean")
        bits = _extract_lsb_bits(arr, max_bits=8 * 512)
        raw = _bits_to_bytes(bits)
        decoded = _try_decode_text(raw)

        payload_note = (
            "Extração sequencial LSB (até 512 bytes). "
            "Payload legível não prova intenção; ausência não prova limpeza."
        )
        if decoded.get("payload_text"):
            summary = summary + " Possível texto recuperado dos LSBs."
            if status == "clean":
                status = "suspicious"

        result = {
            "title": "Camada de Esteganografia (LSB)",
            "status": status,
            "summary": summary,
            "score": round(overall_score, 3),
            "channels": channels_info,
            "image_size": {"width": w, "height": h},
            "methods": ["lsb_bitplane", "entropy", "sequential_extract"],
            "note": (
                "Detecção estatística + tentativa de extração. "
                "Não constitui prova definitiva de mensagem oculta. "
                + payload_note
            ),
            **decoded,
        }
        return result

    except Exception as e:
        return {
            "title": "Camada de Esteganografia (LSB)",
            "status": "error",
            "summary": f"Falha na análise LSB: {e}",
            "score": 0.0,
            "channels": {},
            "methods": [],
            "note": "Erro durante o processamento.",
            "payload_text": None,
            "payload_preview": None,
        }
