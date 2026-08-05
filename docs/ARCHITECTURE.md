# 🏗️ Arquitetura — Sublima Decryptor

## Visão em camadas

```
Frontend (Next.js 15 + Tailwind + shadcn + Three.js)
        |
API Gateway (FastAPI) — Auth · Rate limit · Jobs
        |
   +----+----+----+
   |         |         |
Ingestão   Análise   Interpretação
(files)   (visão,    (LLM + semiótica)
           stego,
           OCR)
        |
PostgreSQL + pgvector
```

## Fluxo de uma análise

1. Upload → validação → armazenamento temporário
2. Ingestão → metadados + hash + pré-processamento
3. Análise técnica → estego, frequência, OCR, features
4. Interpretação → Motor de Decodificação (system prompt + LLM + visão)
5. Síntese → camadas (literal / simbólica / geopolítica / memética)
6. Relatório → Markdown + PDF + árvore 3D opcional

## Princípios

- Privacidade primeiro (modo local)
- Camadas explícitas (fato / inferência / hipótese)
- Auditável (cada conclusão ancora em evidência)
- Extensível (plugins de detectores)

## Referências

- `prompts/SYSTEM_PROMPT.md`
- `docs/USER_STORIES.md`
- `docs/ROADMAP.md`
