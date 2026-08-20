# Changelog — Sublima Decryptor

## [0.3.0] — 2026-08-20

### Ordem 2 — Estabilização (DcsProducer® portfolio)

- **Health** enriquecido (`status` ok/degraded, capabilities, stego_lsb)
- **LSB** integrado no relatório forense (`layers.steganography`)
- **Disclaimer** forense reforçado com marca DcsProducer®
- **Upload**: rejeita arquivo vazio; mensagens de erro mais claras
- **Testes** mínimos: health, analyze PNG, rejeições
- Versão unificada **0.3.0** (API root, health, meta do relatório)

### Critério de pronto v0.3

- [x] Health e `/api/analyze` estáveis
- [x] OCR com caminho de teste (quando Tesseract presente)
- [x] Relatório em camadas + disclaimer
- [x] LSB básico no pipeline
- [ ] Tag `v0.3.0` + redeploy Render (operacional — após merge)

## [0.2.2-ocr] — anterior

OCR Tesseract, deploy Render, visão opcional.
