# Fase 3 — Esteganografia (LSB / DCT)

**Status:** Em início  
**Objetivo:** Detectar e (futuramente) extrair mensagens ocultas em imagens via técnicas clássicas de esteganografia.

---

## 1. Escopo da Fase 3

### 3.1 Detecção (prioridade)
- Análise de LSB (Least Significant Bit) em canais RGB
- Histogramas e estatísticas de bits menos significativos
- Detecção de padrões anômalos (chi-square, RS analysis básico)
- Flag de suspeita + score de confiança

### 3.2 Extração (posterior)
- Extração de payload quando a técnica for identificada com alta confiança
- Suporte inicial a mensagens de texto embutidas via LSB sequencial

### 3.3 Fora de escopo (por enquanto)
- DCT / domínio da frequência (planejado como 3.2)
- Áudio e vídeo
- Esteganografia adaptativa / IA-generated

---

## 2. Estrutura de código proposta

```
backend/app/services/
├─ steganography/
│   ├─ __init__.py
│   ├─ lsb.py          # análise e extração LSB
│   ├─ stats.py        # chi-square, entropia, histograma de bits
│   └─ report.py       # formatação da camada de esteganografia
```

Integração no `image_analyzer.py`:
- Nova chave em `layers["steganography"]`
- Status: `ok` | `suspicious` | `clean` | `error`

---

## 3. Camada de relatório (exemplo de saída)

```json
"steganography": {
  "title": "Camada de Esteganografia",
  "status": "suspicious",
  "summary": "Padrão de bits menos significativos anômalo detectado no canal azul.",
  "methods": ["lsb_analysis", "chi_square"],
  "score": 0.72,
  "details": {
    "lsb_entropy": 0.98,
    "chi_square_p": 0.03,
    "channels": {"R": "normal", "G": "normal", "B": "anomalous"}
  },
  "note": "Detecção estatística — não constitui prova definitiva de mensagem oculta."
}
```

---

## 4. Roadmap interno da Fase 3

| Etapa | Descrição | Prioridade |
|-------|-----------|------------|
| 3.0 | Estrutura de pastas + design (este documento) | Feito |
| 3.1 | `lsb.py` — extração de planos de bit + estatísticas básicas | Alta |
| 3.2 | Teste chi-square / entropia | Alta |
| 3.3 | Integração no `image_analyzer` + nova camada | Alta |
| 3.4 | Testes com imagens conhecidas (cover + stego) | Média |
| 3.5 | DCT básico (opcional) | Baixa (posterior) |

---

## 5. Referências técnicas rápidas

- LSB Steganography (clássico)
- Chi-square attack (Westfeld & Pfitzmann)
- RS Analysis (Fridrich et al.) — versão simplificada
- Pillow + NumPy para manipulação de bits

---

## 6. Disclaimer de uso

A detecção de esteganografia é **probabilística**.  
Falsos positivos e negativos são esperados.  
Resultados devem ser tratados como hipóteses analíticas, nunca como prova definitiva.

---

*Documento inicial da Fase 3 — Producer DCS® / Sublima Decryptor*
