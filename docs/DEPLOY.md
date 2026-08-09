# Deploy — Sublima Decryptor

## Railway (recomendado)

1. [railway.app](https://railway.app) → New Project → Deploy from GitHub → `producerdcs-cpu/sublima-decryptor`
2. Dockerfile na raiz (já configurado em `railway.toml`)
3. Env vars opcionais: `XAI_API_KEY` ou `OPENAI_API_KEY`
4. Health: `/api/health`

## Docker local

```bash
docker build -t sublima-decryptor .
docker run -p 8000:8000 -e XAI_API_KEY=xai-... sublima-decryptor
```

## Frontend

Publique `frontend/` no Vercel/Netlify ou abra local com:
```js
window.SUBLIMA_API = 'https://sua-api.up.railway.app';
```
