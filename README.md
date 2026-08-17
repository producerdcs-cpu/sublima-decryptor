# 🔮 Sublima Decryptor

<p align="center">
  <img src="https://raw.githubusercontent.com/producerdcs-cpu/sublima-decryptor/main/assets/logo.svg" alt="Sublima Decryptor" width="100%"/>
</p>

**A Luz que Revela o que está Oculto**

> Plataforma de análise forense digital, esteganografia, semiótica computacional e decodificação de mensagens subliminares.

**Producer DCS®** | v0.2.2-ocr — OCR + Deploy-ready  
**Licença:** MIT  
**Repositório:** [producerdcs-cpu/sublima-decryptor](https://github.com/producerdcs-cpu/sublima-decryptor)

---

## 📁 Links de Produção

| Recurso | URL |
|---------|-----|
| **Swagger UI (recomendado)** | https://sublima-decryptor.onrender.com/docs |
| API Root (status JSON) | https://sublima-decryptor.onrender.com |
| Health | https://sublima-decryptor.onrender.com/api/health |
| Analyze | `POST` /api/analyze |

> A raiz (`/`) retorna JSON de status. Use **`/docs`** para interagir com a API.

---

## 🎯 O que é

O **Sublima Decryptor** detecta, extrai e interpreta códigos subliminares, esteganográficos e mensagens ocultas em imagens, vídeo, áudio e documentos.

## ✨ Capacidades (MVP atual)

1. **OCR** (Tesseract por+eng) + detecção de microtexto  
2. **Metadados** EXIF + cores dominantes  
3. **Visão / LLM** opcional (XAI ou OpenAI) para camadas simbólicas  
4. Relatório em camadas + disclaimer forense  
5. **Esteganografia LSB** (Fase 3 em andamento)

## 🚀 Deploy

| Plataforma | Guia |
|------------|------|
| **Render (free)** | New Web Service → Docker → health `/api/health` |
| **Railway** | `railway.toml` + Dockerfile |
| **Local** | `docker build -t sublima . && docker run -p 8000:8000 sublima` |

Detalhes: [docs/DEPLOY.md](docs/DEPLOY.md)

## 📁 Estrutura

```
sublima-decryptor/
├─ backend/          # FastAPI + OCR + visão + stego
├─ frontend/         # Upload UI
├─ docs/
├─ Dockerfile
├─ render.yaml
└─ railway.toml
```

## © Autoria

**© 2026 Producer DCS® / DcsProducer® Creative Studio**  
Código sob licença MIT. Nome do produto, marca e identidade visual reservados.  
Commits neste repositório documentam autoria técnica e linha do tempo.

**Sublima Decryptor** — *O que está oculto merece ser compreendido, não temido.*
