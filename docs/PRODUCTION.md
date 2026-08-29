# Production — Sublima Decryptor

**Status:** LIVE  
**Go-live v0.3.0:** 2026-08-29  
**Platform:** Render (Free) · Docker · Oregon  
**URL:** https://sublima-decryptor.onrender.com  
**Version:** **0.3.0**  
**Producer DCS® / DcsProducer®**

## Health (validado 2026-08-29)

```json
{
  "status": "ok",
  "service": "Sublima Decryptor API",
  "phase": "v0.3-stable",
  "version": "0.3.0",
  "brand": "© DcsProducer®",
  "vision_configured": false,
  "ocr_available": true,
  "stego_lsb": true,
  "capabilities": {
    "technical": true,
    "ocr": true,
    "vision": false,
    "steganography_lsb": true
  }
}
```

- `GET /api/health` → 200  
- `GET /docs` → Swagger UI  
- `POST /api/analyze` → relatório com `layers.steganography`

## Checklist de lançamento v0.3.0

| Passo | Status |
|-------|--------|
| Código 0.3.0 em `main` | ✅ |
| LSB no pipeline | ✅ |
| Testes locais 5/5 | ✅ |
| Redeploy Render | ✅ 2026-08-29 |
| Health produção = `0.3.0` | ✅ |
| Tag `v0.3.0` no GitHub | ⏳ se ainda não publicada |

## Testes de produção anteriores

### First (0.2.2-ocr) — 2026-08-12
| File | neurolumen-logo-brain.png |
| HTTP | 200 |

### Second (self-cover) — 2026-08-16
| File | IMG_20260814_131019.jpg |
| OCR | 48 palavras · confidence_avg 84.7 |
| HTTP | 200 |

> Detalhes: [examples/self-cover-ocr-2026-08-16.md](../examples/self-cover-ocr-2026-08-16.md)

## Notes

- Free tier: cold start ~50s após inatividade.
- Visão ativa com `XAI_API_KEY` ou `OPENAI_API_KEY` no Render.
- © 2026 Producer DCS® / DcsProducer® Creative Studio
