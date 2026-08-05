# 🗺️ Roadmap — Sublima Decryptor

## Visão geral

| Fase | Nome | Status | Entrega principal |
|------|------|--------|-------------------|
| 0 | Foundation | ✅ | Docs, prompts, exemplo Economist, repo |
| 1 | MVP | 📋 | Upload de imagem → análise simbólica + relatório |
| 2 | Multimodal | 📋 | Áudio, vídeo, PDF, metadados, OCR |
| 3 | Deep Scan | 📋 | Múltiplos modelos, esteganografia, árvore 3D |
| 4 | Plataforma | 📋 | API, histórico, comunidade, deploy |

---

## Fase 0 — Foundation (concluída)

- [x] Nome, slogan e posicionamento
- [x] README e arquitetura
- [x] System prompt do Motor de Decodificação
- [x] User stories
- [x] Análise-exemplo: capa The Economist 2026
- [x] Repositório público no GitHub

## Fase 1 — MVP

- [ ] Frontend Next.js (upload + preview + painel de camadas)
- [ ] Backend FastAPI (endpoint de análise de imagem)
- [ ] Integração com modelo de visão + LLM para interpretação simbólica
- [ ] Relatório em Markdown/PDF (camadas: literal, simbólica, geopolítica)
- [ ] Histórico local simples

## Fase 2 — Multimodal

- [ ] Pipeline de áudio (espectrograma + Whisper)
- [ ] Frames de vídeo + timeline de símbolos
- [ ] Extração de metadados (EXIF, XMP, PDF comments)
- [ ] OCR avançado + detecção de microtexto
- [ ] Suporte a lote (batch)

## Fase 3 — Deep Scan & Esteganografia

- [ ] Detectores LSB / DCT / F5
- [ ] Visualização radial / globo 3D (Three.js)
- [ ] Comparação com base de simbolismo (embeddings)
- [ ] Modo privacidade com modelos locais

## Fase 4 — Plataforma

- [ ] API pública (auth + rate limit)
- [ ] Conta de usuário + histórico versionado
- [ ] Export forense profissional
- [ ] Deploy (Vercel + Railway/AWS)

---

**Última atualização:** 05/08/2026  
**Versão atual:** v0.1.0 — Foundation
