# Deploy — Sublima Decryptor

## 1. Render (recomendado no plano free)

1. https://render.com → **New** → **Web Service**
2. Conecte GitHub → `producerdcs-cpu/sublima-decryptor`
3. **Runtime:** Docker
4. **Dockerfile path:** `./Dockerfile`
5. **Health Check Path:** `/api/health`
6. (Opcional) `XAI_API_KEY` ou `OPENAI_API_KEY`
7. **Create Web Service** → build ~2–4 min (Tesseract)
8. URL: `https://sublima-decryptor-xxxx.onrender.com`

```bash
curl https://SUA-URL.onrender.com/api/health
```

> Free: dorme após ~15 min (cold start 30–60 s).

## 2. Railway

`Dockerfile` + `railway.toml`. Free costuma ter 1 projeto — se NeuroLeitor ocupa, use Render.

## 3. Docker local

```bash
docker build -t sublima-decryptor .
docker run -p 8000:8000 sublima-decryptor
```
