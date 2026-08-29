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
- [x] **Redeploy produção v0.3.0** — 2026-08-29  
  Health: `version: "0.3.0"` · `phase: "v0.3-stable"` · `stego_lsb: true`
- [x] **Tag + Release `v0.3.0`** — 2026-08-29  
  https://github.com/producerdcs-cpu/sublima-decryptor/releases/tag/v0.3.0
- [x] **Frontend apontando para URL de produção** — 2026-08-29  
  `frontend/index.html` → `https://sublima-decryptor.onrender.com` + camada stego
- [x] **Extração de payload LSB** — 2026-08-29  
  Extração sequencial + tentativa de texto (utf-8/latin-1/ascii)

## Next (backlog)

- [ ] Redeploy Render para ativar extração de payload em produção
- [ ] Auth + rate limit se tráfego crescer
- [ ] Fase 2 — pré-processamento / microtexto reforçado

## Produção

Ver [PRODUCTION.md](PRODUCTION.md) · [V0_3.md](V0_3.md) · [CHANGELOG.md](../CHANGELOG.md)
