import pandas as pd

class IAMaquina:
    def analisar(self, df: pd.DataFrame):
        if "nivel" not in df.columns:
            raise ValueError("Coluna 'nivel' ausente.")
        self.media = df["nivel"].mean()

    def decisao(self):
        if self.media > 5:
            return "AMEAÇA: ALTA. AÇÃO NECESSÁRIA."
        return "AMEAÇA: BAIXA. CONTINUAR MONITORAMENTO."
