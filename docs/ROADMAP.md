# Roadmap — Sublima Decryptor

## Done

- [x] MVP upload + relatório técnico (EXIF, cores, dimensões)
- [x] Fase 1.1 — integração visão (OpenAI-compatible / xAI)
- [x] Fase 1.2 — OCR Tesseract (por+eng) + microtexto
- [x] Docker + Railway config
- [x] **Deploy produção Render** — 2026-08-12  
  https://sublima-decryptor.onrender.com  
  Health OK · OCR live · POST /api/analyze validado
- [x] Auditoria de produção automatizada (GitHub Actions)

## In Progress

- [ ] **Fase 3 — Esteganografia (LSB/DCT)** — design iniciado  
  Ver [FASE_3_ESTEGANOGRAFIA.md](FASE_3_ESTEGANOGRAFIA.md)

## Next

- [ ] Frontend apontando para URL de produção
- [ ] Env `XAI_API_KEY` (opcional) para camadas simbólicas
- [ ] Fase 2 — pré-processamento de imagem / microtexto reforçado
- [ ] Auth + rate limit (se uso público crescer)

## Produção

Ver [PRODUCTION.md](PRODUCTION.md)
