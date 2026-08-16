# Exemplo de análise — Self-Cover OCR (capa do Sublima Decryptor)

**Fonte:** captura da capa / branding do próprio produto (IMG_20260814_131019.jpg)  
**Tipo:** foto de tela (JPEG)  
**Data de referência:** 16/08/2026  
**Endpoint:** `POST https://sublima-decryptor.onrender.com/api/analyze`  
**Versão:** 0.2.2-ocr

---

## 1. Resumo literal

Imagem JPEG 720×1421 px, modo RGB, densidade visual alta. Sem metadados EXIF. OCR extraiu com sucesso o texto do branding e do README do projeto.

## 2. Metadados técnicos

| Campo | Valor |
|-------|-------|
| Arquivo original | IMG_20260814_131019.jpg |
| Formato | JPEG |
| Dimensões | 720 × 1421 |
| Tamanho | 87.744 bytes |
| Densidade visual | alta |
| EXIF | ausente |
| OCR disponível | true |
| Visão configurada | false |

## 3. OCR / Texto extraído (resumo)

```
README /

Sublima Decryptor

A Luz que Revela o que está Oculto

Plataforma de análise forense
digital, esteganografia,
semiótica computacional e
decodificação de mensagens
subliminares.

Producer DCS® | v0.2.2-ocr — OCR +
Deploy-ready

Licença: MIT

Repositório: producerdcs-
cpu/sublima-decryptor
```

- **Palavras:** 48  
- **Confiança média:** 84.7  
- **Possível microtexto:** true  
- **Engine:** tesseract

## 4. Camada literal

Imagem JPEG 720×1421px, modo RGB. Densidade visual alta.  
Fatos:
- Dimensões: 720 × 1421
- Formato: JPEG
- Arquivo: IMG_20260814_131019.jpg
- Tamanho: 87744 bytes
- OCR: 48 palavras extraídas
- Possível microtexto detectado

## 5. Camadas simbólicas / geopolítica / memética / hipóteses

Status: `pending_vision_model` (XAI_API_KEY ou OPENAI_API_KEY não configurada no ambiente de produção no momento do teste).

## 6. Valor deste teste

- Validação autorreferencial: o sistema leu corretamente o próprio material de branding.
- Confirma robustez do OCR em captura de tela real (não apenas imagens limpas).
- Serve como baseline de regressão para futuras alterações no pipeline OCR.
- Demonstra que a Fase 1.2-OCR está estável em produção.

## 7. Disclaimer

> Interpretações além da camada literal são hipóteses analíticas. Não constituem prova de intenção do autor nem de conspiração.

## 8. Próximos passos sugeridos

1. Configurar `XAI_API_KEY` para preencher camadas simbólicas neste mesmo arquivo.
2. Usar este exemplo como imagem padrão de teste OCR em CI (quando disponível).
3. Fase 3 — esteganografia (LSB/DCT).

---

*Documento gerado a partir da resposta real da API em 16/08/2026 · Producer DCS®*
