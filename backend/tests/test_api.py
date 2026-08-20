"""Testes de estabilidade v0.3 — health + analyze técnico + LSB."""
from __future__ import annotations

import io
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from PIL import Image

# Garante import do pacote app/
BACKEND = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND))

from app.main import app  # noqa: E402

client = TestClient(app)


def _png_bytes(size=(64, 64), color=(30, 120, 200)) -> bytes:
    buf = io.BytesIO()
    Image.new("RGB", size, color).save(buf, format="PNG")
    return buf.getvalue()


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    data = r.json()
    assert data["service"] == "Sublima Decryptor"
    assert data["version"].startswith("0.3")
    assert "links" in data


def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] in ("ok", "degraded")
    assert data["version"].startswith("0.3")
    assert data.get("stego_lsb") is True
    assert "ocr_available" in data
    assert "capabilities" in data


def test_analyze_png():
    content = _png_bytes()
    r = client.post(
        "/api/analyze",
        files={"file": ("fixture.png", content, "image/png")},
    )
    assert r.status_code == 200
    data = r.json()
    assert data["meta"]["version"].startswith("0.3")
    assert "layers" in data
    assert "literal" in data["layers"]
    assert "steganography" in data["layers"]
    assert data["layers"]["steganography"].get("status") in (
        "clean",
        "suspicious",
        "error",
    )
    assert "disclaimer" in data
    assert "DcsProducer" in data["disclaimer"] or "hipóteses" in data["disclaimer"].lower()
    assert data.get("file_id")


def test_analyze_reject_empty():
    r = client.post(
        "/api/analyze",
        files={"file": ("empty.png", b"", "image/png")},
    )
    assert r.status_code == 400


def test_analyze_reject_bad_ext():
    r = client.post(
        "/api/analyze",
        files={"file": ("x.exe", b"MZ", "application/octet-stream")},
    )
    assert r.status_code == 400
