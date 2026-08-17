# Anúncio Oficial — Sublima Decryptor

**Producer DCS®** | Agosto 2026

---

## Status atual

O **Sublima Decryptor** encontra-se em produção com a **Fase 1.2 (OCR)** estável.

### Links úteis

| Recurso | URL |
|---------|-----|
| **Swagger UI (recomendado)** | https://sublima-decryptor.onrender.com/docs |
| API Root (JSON de status) | https://sublima-decryptor.onrender.com |
| Health check | https://sublima-decryptor.onrender.com/api/health |
| Endpoint de análise | `POST` https://sublima-decryptor.onrender.com/api/analyze |
| Repositório | https://github.com/producerdcs-cpu/sublima-decryptor |

> **Nota:** A raiz (`/`) retorna JSON de status da API. Para interagir visualmente use sempre **`/docs`**.

- OCR (Tesseract) operacional
- Relatório em camadas + disclaimer forense
- Auditoria de produção automatizada via GitHub Actions
- Fase 3 (Esteganografia LSB) iniciada

---

## Convite a feedback

Este espaço (e as **Discussions** do repositório, quando ativadas) serve para:

- Relatar usos reais e casos de teste
- Sugerir melhorias na detecção de esteganografia
- Compartilhar imagens de referência (cover / stego)
- Discutir prioridades da Fase 3 e seguintes

Feedbacks técnicos e de produto são bem-vindos.

---

## Como contribuir ou comentar

1. Abra uma **Discussion** (recomendado) ou uma Issue
2. Use a categoria adequada (Ideias, Casos de uso, Bugs)
3. Seja objetivo e, se possível, anexe evidências

---

## Próximas etapas visíveis

- Integração da camada de esteganografia no relatório JSON
- Melhoria das métricas estatísticas (chi-square etc.)
- Frontend apontando para a URL de produção

Obrigado pelo interesse.

**Producer DCS®**  
*O que está oculto merece ser compreendido, não temido.*
