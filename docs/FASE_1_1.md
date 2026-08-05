# Fase 1.1 — Modelo de visão no analyzer

## O que mudou

- `backend/app/services/vision.py` — cliente OpenAI-compatible (xAI/Grok, OpenAI)
- `image_analyzer.py` preenche camadas simbólicas quando há API key
- Sem key: camada literal + status `not_configured`

## Ativar

```bash
export XAI_API_KEY=xai-...
# ou OPENAI_API_KEY=sk-...
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Ver `.env.example` para opções de modelo.
