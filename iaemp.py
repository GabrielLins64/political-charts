"""Gráfico do IAEmp por período
Dados extraídos do site da FGV IBRE.
https://portalibre.fgv.br/noticias/iaemp-sobe-08-ponto-em-fevereiro

Para executar:
1. Instale o Python
2. Instale o gerenciador de pacotes python PIP
3. Instale o matplotlib com o PIP (pip install matplotlib)
4. Execute o programa com "python iaemp.py"
"""

import matplotlib.pyplot as plt
from file_handler import open_xy_csv
import numpy as np


FILEPATH = "data/iaemp.csv"
SHOWN_PERIODS = 20


if __name__ == '__main__':
    periodos, iaemp = open_xy_csv(FILEPATH)

    plt.plot(periodos, iaemp)
    plt.xlabel('Período')
    plt.ylabel('IAEmp')
    plt.title('Indicador Antecedente de Emprego (IAEmp)')

    shown_indexes = np.linspace(0, len(periodos) - 1, SHOWN_PERIODS, dtype=int)
    plt.xticks(shown_indexes)

    plt.show()
