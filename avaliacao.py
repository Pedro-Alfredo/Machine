import numpy as np

class Avaliacao:
    def __init__(self, dados):
        self.dados = np.array(dados)

    def media(self):
        return float(np.mean(self.dados))
