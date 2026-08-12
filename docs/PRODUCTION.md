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
- `POST /api/analyze` → 200 (tested with `neurolumen-logo-brain.png`)

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

## Notes

- Free tier spins down after inactivity (~50s cold start).
- Vision layers activate when `XAI_API_KEY` or `OPENAI_API_KEY` is set in Render Environment.
- © 2026 Producer DCS® / DcsProducer® Creative Studio
