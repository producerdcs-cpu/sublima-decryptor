"""Estatísticas auxiliares para detecção de esteganografia.

Será expandido com chi-square e outras métricas na próxima iteração.
"""
from __future__ import annotations

import numpy as np


def chi_square_basic(plane: np.ndarray) -> float:
    """Placeholder — chi-square simplificado sobre histograma de bits.

    Retorna p-value aproximado (quanto menor, mais suspeito).
    Implementação completa virá na etapa 3.2.
    """
    # Versão mínima: apenas retorna 1.0 (não suspeito) por enquanto
    return 1.0
