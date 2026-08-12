# Roadmap — Sublima Decryptor

## Done

- [x] MVP upload + relatório técnico (EXIF, cores, dimensões)
- [x] Fase 1.1 — integração visão (OpenAI-compatible / xAI)
- [x] Fase 1.2 — OCR Tesseract (por+eng) + microtexto
- [x] Docker + Railway config
- [x] **Deploy produção Render** — 2026-08-12  
  https://sublima-decryptor.onrender.com  
  Health OK · OCR live · POST /api/analyze validado

## Next

- [ ] Frontend apontando para URL de produção
- [ ] Env `XAI_API_KEY` (opcional) para camadas simbólicas
- [ ] Fase 2 — pré-processamento de imagem / microtexto reforçado
- [ ] Fase 3 — esteganografia LSB/DCT
- [ ] Auth + rate limit (se uso público crescer)

## Produção

Ver [PRODUCTION.md](PRODUCTION.md)
