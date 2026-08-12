# Apostila resumida — Sublima Decryptor

**Versão do produto:** v0.2.2-ocr  
**Produção:** https://sublima-decryptor.onrender.com  
**Repositório:** https://github.com/producerdcs-cpu/sublima-decryptor  

**© 2026 DcsProducer® / Producer DCS® Creative Studio**  
Nome do produto, marca e identidade visual reservados.  
Código sob licença MIT; autoria técnica documentada pelos commits deste repositório.

---

## 1. O que é

O **Sublima Decryptor** é uma plataforma de **análise forense digital** de imagens.  
Objetivo: extrair o que está visível e o que pode estar oculto ou pouco evidente — texto (OCR), metadados, cores e, quando configurado, leitura simbólica assistida por modelo de visão.

Slogan: *A Luz que Revela o que está Oculto.*

**Posicionamento:** ferramenta analítica e educacional.  
Não afirma conspiração nem intenção do autor. Interpretações além do literal são **hipóteses**, com disclaimer explícito em cada relatório.

---

## 2. Estado atual (ciclo de foco)

| Item | Situação |
|------|----------|
| API em produção | **Online** (Render free) |
| OCR (Tesseract por+eng) | **Ativo** |
| Microtexto (heurística) | **Ativo** |
| Metadados EXIF + cores | **Ativo** |
| Visão / camadas simbólicas | **Opcional** (desligado sem API key) |
| Frontend estático | Existe em `frontend/`; uso principal via `/docs` |
| Custo de hospedagem | **R$ 0** (free; dorme após ~15 min sem uso) |

Health esperado:

```json
{
  "status": "ok",
  "version": "0.2.2-ocr",
  "ocr_available": true,
  "vision_configured": false
}
```

---

## 3. Como funciona (visão geral)

```
Imagem (upload)
    → Metadados técnicos (tamanho, formato, EXIF, cores)
    → OCR (texto + possível microtexto)
    → [Opcional] Modelo de visão (camadas simbólica / narrativa / memética)
    → Relatório JSON em camadas + disclaimer
```

### Camadas do relatório

| Camada | Conteúdo |
|--------|----------|
| **Literal** | Dimensões, formato, arquivo, fatos OCR |
| **OCR** | Texto extraído, contagem, confiança, microtexto |
| **Simbólica** | Elementos visuais (se visão configurada) |
| **Geopolítica / narrativa** | Leitura de contexto (se visão) |
| **Memética** | Referências de cultura/meme (se visão) |
| **Hipóteses** | Sugestões com ressalva — não são fatos |

---

## 4. Como utilizar

### 4.1 Pelo Swagger (recomendado no MVP)

1. Abra: https://sublima-decryptor.onrender.com/docs  
2. Na primeira visita do dia pode haver **cold start** (30–60 s) — aguarde.  
3. Expanda `POST /api/analyze`.  
4. **Try it out** → escolha um arquivo de imagem (`arquivo`).  
5. **Execute**.  
6. Resposta **200** traz o JSON completo do relatório.

### 4.2 Pela API (curl)

```bash
curl -X POST "https://sublima-decryptor.onrender.com/api/analyze" \
  -F "file=@sua-imagem.png"
```

### 4.3 Health

```bash
curl https://sublima-decryptor.onrender.com/api/health
```

### 4.4 Frontend local (opcional)

Abra `frontend/index.html` e aponte a API:

```js
window.SUBLIMA_API = "https://sublima-decryptor.onrender.com";
```

---

## 5. O que já funciona bem / limites do MVP

**Funciona**
- Upload de imagem e relatório técnico  
- OCR em português e inglês  
- Detecção heurística de microtexto  
- Deploy Docker no Render  

**Ainda não (ou parcial)**
- Camadas simbólicas sem `XAI_API_KEY` / `OPENAI_API_KEY`  
- Vídeo, áudio e PDF multipágina (visão de produto; fora do MVP atual)  
- Esteganografia LSB/DCT (roadmap Fase 3)  
- Conta de usuário / histórico persistente (filesystem free é efêmero)  

---

## 6. Roteiro rápido — 5 usuários (ciclo de foco)

Objetivo: validar uso real, não desenvolver feature nova.

1. Envie o link `/docs` para 5 pessoas.  
2. Peça: *“Envie uma imagem (foto, meme ou capa) e diga o que acharam do relatório.”*  
3. Anote: travou? cold start incomodou? OCR útil? pediram “significado oculto”?  
4. Não prometa visão simbólica ligada neste ciclo.  
5. Ao final: 5 feedbacks → decisão de manter foco, ajustar UX, ou passar ao próximo da fila.

---

## 7. Marca e autoria

```
© 2026 DcsProducer® / Producer DCS® Creative Studio
Sublima Decryptor — produto e identidade reservados.
Código: MIT · Autoria técnica: repositório producerdcs-cpu/sublima-decryptor
```

Em comunicações públicas, preferir:

> Sublima Decryptor · © DcsProducer®  
> A Luz que Revela o que está Oculto

---

## 8. Links úteis

| Recurso | URL |
|---------|-----|
| Produção | https://sublima-decryptor.onrender.com |
| API Docs | https://sublima-decryptor.onrender.com/docs |
| Health | https://sublima-decryptor.onrender.com/api/health |
| GitHub | https://github.com/producerdcs-cpu/sublima-decryptor |
| Deploy | [docs/DEPLOY.md](DEPLOY.md) |
| Produção (log) | [docs/PRODUCTION.md](PRODUCTION.md) |
| Roadmap | [docs/ROADMAP.md](ROADMAP.md) |

---

*Documento de ciclo de foco — não substitui o README técnico completo.*  
**DcsProducer® Creative Studio** · Inteligência Artificial · Design · Criatividade · Inovação
