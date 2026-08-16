# Production — Sublima Decryptor

**Status:** LIVE  
**Deployed:** 2026-08-12  
**Platform:** Render (Free)  
**URL:** https://sublima-decryptor.onrender.com  
**Version:** 0.2.2-ocr  
**Producer DCS®**

## Health (validated)

```json
{
  "status": "ok",
  "service": "Sublima Decryptor API",
  "phase": "1.2-ocr",
  "version": "0.2.2-ocr",
  "vision_configured": false,
  "ocr_available": true
}
```

- `GET /api/health` → 200  
- `GET /docs` → Swagger UI  
- `POST /api/analyze` → 200 (tested with `neurolumen-logo-brain.png` and self-cover)

## First production analyze test

| Field | Value |
|-------|-------|
| Date | 2026-08-12 ~10:52 UTC |
| File | neurolumen-logo-brain.png |
| Format | JPEG (from PNG upload) |
| Dimensions | 1165 × 784 |
| OCR | available: true |
| Vision | not_configured (no API key) |
| HTTP | 200 |

## Second production analyze test (self-cover)

| Field | Value |
|-------|-------|
| Date | 2026-08-16 ~19:42 UTC |
| File | IMG_20260814_131019.jpg (capa / captura do branding) |
| Format | JPEG |
| Dimensions | 720 × 1421 |
| OCR | 48 palavras · confidence_avg 84.7 · possible_microtext=true |
| Vision | not_configured |
| HTTP | 200 |
| Nota | Extração bem-sucedida do texto do README/branding (teste autorreferencial de qualidade) |

> Detalhes completos: [examples/self-cover-ocr-2026-08-16.md](../examples/self-cover-ocr-2026-08-16.md)

## Notes

- Free tier spins down after inactivity (~50s cold start).
- Vision layers activate when `XAI_API_KEY` or `OPENAI_API_KEY` is set in Render Environment.
- O segundo teste valida a robustez do OCR em captura de tela real do próprio produto.
- © 2026 Producer DCS® / DcsProducer® Creative Studio
