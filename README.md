# 🔮 Sublima Decryptor

<p align="center">
  <img src="https://raw.githubusercontent.com/producerdcs-cpu/sublima-decryptor/main/assets/logo.svg" alt="Sublima Decryptor" width="100%"/>
</p>

**A Luz que Revela o que está Oculto**

> Plataforma de análise forense digital, esteganografia, semiótica computacional e decodificação de mensagens subliminares.

**DcsProducer® Creative Studio** | **v0.3.0** — estabilidade + LSB no relatório  
**Licença:** All Rights Reserved (ver [LICENSE](LICENSE) · [NOTICE](NOTICE))  
**Repositório:** [producerdcs-cpu/sublima-decryptor](https://github.com/producerdcs-cpu/sublima-decryptor)

> ⚠️ Código **source-available** para portfólio. **Não** é licença permissiva (MIT/Apache). Uso, cópia comercial ou redistribuição exigem autorização escrita.

---

## 📁 Links de Produção

| Recurso | URL |
|---------|-----|
| **Swagger UI** | https://sublima-decryptor.onrender.com/docs |
| API Root | https://sublima-decryptor.onrender.com |
| Health | https://sublima-decryptor.onrender.com/api/health |
| Analyze | `POST` /api/analyze |

---

## ✨ Capacidades (v0.3)

1. **OCR** (Tesseract por+eng) + microtexto  
2. **Metadados** EXIF + cores dominantes  
3. **Visão / LLM** opcional (XAI ou OpenAI)  
4. **Relatório em camadas** + disclaimer forense  
5. **Esteganografia LSB** (score estatístico por canal)  
6. Testes mínimos de regressão (`backend/tests`)

## 🚀 60 segundos (local)

```bash
cd backend
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload --port 8000
# abra http://localhost:8000/docs
```

## Deploy

| Plataforma | Guia |
|------------|------|
| **Render** | Docker · health `/api/health` |
| **Railway** | `railway.toml` |
| **Local** | `docker build -t sublima . && docker run -p 8000:8000 sublima` |

Detalhes: [docs/DEPLOY.md](docs/DEPLOY.md) · [docs/V0_3.md](docs/V0_3.md) · [CHANGELOG.md](CHANGELOG.md)

## © Autoria e marca

**© 2026 DcsProducer® Creative Studio**  
Licença: **All Rights Reserved** — ver [LICENSE](LICENSE) e [NOTICE](NOTICE).  
Nome do produto, logotipo e identidade visual reservados.

**Sublima Decryptor** — *O que está oculto merece ser compreendido, não temido.*
