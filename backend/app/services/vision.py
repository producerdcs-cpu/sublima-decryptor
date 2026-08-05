"""Vision + LLM client — Fase 1.1"""
from __future__ import annotations

import base64
import json
import os
import re
from pathlib import Path
from typing import Any, Optional

import httpx

SYSTEM_PROMPT = """Você é o Motor de Decodificação do Sublima Decryptor.
Analise a imagem e responda APENAS com JSON válido (sem markdown):
{
  "literal_summary": "descrição objetiva em 2-3 frases",
  "elements": [{"name": "...", "category": "objeto|simbolo|texto|pessoa|outro", "description": "...", "confidence": "alta|media|baixa"}],
  "symbolic": "interpretação simbólica",
  "geopolitical": "leitura geopolítica se houver base visual",
  "memetic": "referências meméticas se houver",
  "hypotheses": [{"text": "...", "confidence": "baixa|media|alta", "evidence": "..."}]
}
Separe fato de hipótese; ancore no visual; não invente; português; tom sóbrio.
"""


def _encode_image(path: str) -> tuple[str, str]:
    p = Path(path)
    b64 = base64.b64encode(p.read_bytes()).decode("ascii")
    suffix = p.suffix.lower().lstrip(".")
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp", "gif": "image/gif"}.get(suffix, "image/jpeg")
    return b64, mime


def vision_configured() -> bool:
    return bool(os.getenv("OPENAI_API_KEY") or os.getenv("XAI_API_KEY") or os.getenv("VISION_API_KEY"))


def _resolve_provider() -> dict[str, str]:
    xai, openai, generic = os.getenv("XAI_API_KEY"), os.getenv("OPENAI_API_KEY"), os.getenv("VISION_API_KEY")
    base = os.getenv("VISION_API_BASE", "")
    if xai:
        return {"api_key": xai, "base_url": base or "https://api.x.ai/v1", "model": os.getenv("VISION_MODEL", "grok-2-vision-1212")}
    if openai:
        return {"api_key": openai, "base_url": base or "https://api.openai.com/v1", "model": os.getenv("VISION_MODEL", "gpt-4o")}
    if generic and base:
        return {"api_key": generic, "base_url": base.rstrip("/"), "model": os.getenv("VISION_MODEL", "gpt-4o")}
    return {}


def _parse_json_response(text: str) -> Optional[dict]:
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if fence:
        text = fence.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except json.JSONDecodeError:
                return None
    return None


async def analyze_with_vision(path: str, technical_context: Optional[dict] = None) -> Optional[dict[str, Any]]:
    provider = _resolve_provider()
    if not provider:
        return None
    b64, mime = _encode_image(path)
    user_text = "Analise esta imagem conforme o formato JSON solicitado."
    if technical_context:
        user_text += f"\n\nContexto técnico: {json.dumps(technical_context, ensure_ascii=False)[:800]}"
    url = f"{provider['base_url']}/chat/completions"
    headers = {"Authorization": f"Bearer {provider['api_key']}", "Content-Type": "application/json"}
    payload = {
        "model": provider["model"],
        "temperature": 0.3,
        "max_tokens": 2000,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": [
                {"type": "text", "text": user_text},
                {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}},
            ]},
        ],
    }
    try:
        async with httpx.AsyncClient(timeout=90.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            content = resp.json()["choices"][0]["message"]["content"]
            parsed = _parse_json_response(content)
            if parsed:
                parsed["_provider"] = {"model": provider["model"], "base_url": provider["base_url"]}
            return parsed
    except Exception as e:
        return {"_error": str(e), "elements": [], "literal_summary": ""}
