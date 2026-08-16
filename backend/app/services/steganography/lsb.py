"""Análise LSB (Least Significant Bit) — Fase 3.1

Objetivo atual:
- Extrair planos de bit menos significativos dos canais RGB
- Calcular estatísticas básicas (entropia, proporção de bits)
- Retornar score de suspeita + detalhes por canal

Ainda não faz extração de payload (virá depois).
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


def analyze_lsb(path: str | Path) -> dict[str, Any]:
    """Analisa os LSBs de uma imagem e retorna relatório estruturado.

    Retorno típico:
    {
      "status": "clean" | "suspicious" | "error",
      "summary": str,
      "score": float,          # 0.0 – 1.0 (maior = mais suspeito)
      "channels": {...},
      "methods": ["lsb_bitplane", "entropy"],
      "note": str
    }
    """
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

            # Heurística simples inicial:
            # - Entropia muito alta + desvio pode indicar payload
            deviation = abs(ent - 0.95)  # valor empírico inicial
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

        return {
            "title": "Camada de Esteganografia (LSB)",
            "status": status,
            "summary": summary,
            "score": round(overall_score, 3),
            "channels": channels_info,
            "image_size": {"width": w, "height": h},
            "methods": ["lsb_bitplane", "entropy"],
            "note": (
                "Detecção estatística preliminar. "
                "Não constitui prova definitiva de mensagem oculta."
            ),
        }

    except Exception as e:
        return {
            "title": "Camada de Esteganografia (LSB)",
            "status": "error",
            "summary": f"Falha na análise LSB: {e}",
            "score": 0.0,
            "channels": {},
            "methods": [],
            "note": "Erro durante o processamento.",
        }
