# Production — Sublima Decryptor

**Status:** LIVE (aguardando redeploy v0.3.0)  
**Deployed (inicial):** 2026-08-12  
**Platform:** Render (Free)  
**URL:** https://sublima-decryptor.onrender.com  
**Código em main:** **0.3.0**  
**Produção observada (29/08):** ainda `0.2.2-ocr` até redeploy  
**Producer DCS® / DcsProducer®**

## Health esperado após redeploy v0.3.0

```json
{
  "status": "ok",
  "service": "Sublima Decryptor API",
  "phase": "v0.3-stable",
  "version": "0.3.0",
  "brand": "© DcsProducer®",
  "vision_configured": false,
  "ocr_available": true,
  "stego_lsb": true
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
| Tag `v0.3.0` no GitHub | ⏳ operador |
| Redeploy Render | ⏳ operador |
| Health produção = `0.3.0` | ⏳ após redeploy |

## Testes de produção anteriores (0.2.2-ocr)

### First production analyze test

| Field | Value |
|-------|-------|
| Date | 2026-08-12 ~10:52 UTC |
| File | neurolumen-logo-brain.png |
| Dimensions | 1165 × 784 |
| OCR | available: true |
| HTTP | 200 |

### Second production analyze test (self-cover)

| Field | Value |
|-------|-------|
| Date | 2026-08-16 ~19:42 UTC |
| File | IMG_20260814_131019.jpg |
| Dimensions | 720 × 1421 |
| OCR | 48 palavras · confidence_avg 84.7 |
| HTTP | 200 |

> Detalhes: [examples/self-cover-ocr-2026-08-16.md](../examples/self-cover-ocr-2026-08-16.md)

## Notes

- Free tier: cold start ~50s após inatividade.
- Visão ativa com `XAI_API_KEY` ou `OPENAI_API_KEY` no Render.
- Após tag + redeploy, atualizar este arquivo com a data real do go-live 0.3.0.
- © 2026 Producer DCS® / DcsProducer® Creative Studio
