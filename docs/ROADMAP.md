# Roadmap — Sublima Decryptor

## Done

- [x] MVP upload + relatório técnico (EXIF, cores, dimensões)
- [x] Fase 1.1 — integração visão (OpenAI-compatible / xAI)
- [x] Fase 1.2 — OCR Tesseract (por+eng) + microtexto
- [x] Docker + Railway / Render
- [x] Deploy produção Render — https://sublima-decryptor.onrender.com
- [x] Auditoria de produção (GitHub Actions)
- [x] **v0.3.0 — estabilidade** (código 2026-08-20, testes 2026-08-29)  
  Health + analyze estáveis · LSB no relatório · disclaimer · testes 5/5

## Lançamento v0.3.0 (em curso)

- [ ] Tag `v0.3.0` + Release no GitHub
- [ ] Redeploy Render
- [ ] Confirmar health produção `version: "0.3.0"`

## Next (pós-lançamento)

- [ ] Frontend apontando para URL de produção
- [ ] Extração de payload LSB (além de score estatístico)
- [ ] Auth + rate limit se tráfego crescer
- [ ] Fase 2 — pré-processamento / microtexto reforçado

## Produção

Ver [PRODUCTION.md](PRODUCTION.md) · [V0_3.md](V0_3.md) · [CHANGELOG.md](../CHANGELOG.md)
