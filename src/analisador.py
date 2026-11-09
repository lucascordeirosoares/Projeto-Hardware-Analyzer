
from pathlib import Path
import pandas as pd


class AnalisadorHardware:
    """Classe responsável por carregar e preparar os dados de hardware."""

    def __init__(self):
        self.pasta_dados = Path(__file__).resolve().parent.parent / "data"
        self.bases = {}

        self.carregar_dados()

    def carregar_dados(self):
        """Carrega e prepara todos os arquivos CSV."""

        for arquivo in self.pasta_dados.glob("*.csv"):
            nome_categoria = arquivo.stem.replace("Data", "")

            df = pd.read_csv(arquivo)

            # Remove registros duplicados
            df = df.drop_duplicates()

            # Remove espaços extras dos textos
            for coluna in df.select_dtypes(include="object").columns:
                df[coluna] = df[coluna].str.strip()

            # Converte os preços para números
            if "Price" in df.columns:
                df["Price"] = (
                    df["Price"]
                    .str.replace("$", "", regex=False)
                    .str.replace(" USD", "", regex=False)
                )

                df["Price"] = pd.to_numeric(
                    df["Price"], errors="coerce"
                )

            self.bases[nome_categoria] = df

            print(f"{nome_categoria}: {len(df)} produtos carregados.")
