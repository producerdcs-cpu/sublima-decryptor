# MVP — Sublima Decryptor v0.2.0

## O que o MVP entrega

1. **API FastAPI** (`backend/`)
   - `GET /api/health`
   - `POST /api/analyze` — upload → relatório JSON em camadas

2. **Frontend estático** (`frontend/index.html`)
   - Upload + preview + relatório

3. **Relatório em camadas**
   - Literal (fatos técnicos)
   - Simbólica / geopolítica / memética / hipóteses (estrutura pronta)
   - Disclaimer forense

## Como rodar

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Frontend: abrir `frontend/index.html` ou `python -m http.server 5173` em `frontend/`.

## Próximo (Fase 1.1)

- Modelo de visão no analyzer
- OCR
- Preencher camadas simbólicas automaticamente
