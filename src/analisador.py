
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

            # Transforma textos vazios em valores ausentes
            df = df.replace(r"^\s*$", pd.NA, regex=True)

            # Remove produtos sem nome
            if "Name" in df.columns:
                df = df.dropna(subset=["Name"])

            # Converte os preços para números
            if "Price" in df.columns:
                df["Price"] = (
                    df["Price"]
                    .astype("string")
                    .str.replace("$", "", regex=False)
                    .str.replace(" USD", "", regex=False)
                )

                df["Price"] = pd.to_numeric(
                    df["Price"], errors="coerce"
                )

            # Preenche informações textuais ausentes
            colunas_texto = df.select_dtypes(include="object").columns
            df[colunas_texto] = df[colunas_texto].fillna("Não informado")

            self.bases[nome_categoria] = df

            print(f"{nome_categoria}: {len(df)} produtos carregados.")

    def obter_estatisticas_preco(self, categoria):
        """Retorna estatísticas dos preços de uma categoria."""

        if categoria not in self.bases:
            raise ValueError("Categoria não encontrada.")

        df = self.bases[categoria]
        precos = df["Price"].dropna()

        if precos.empty:
            return None

        estatisticas = {
            "quantidade": len(precos),
            "media": round(float(precos.mean()), 2),
            "mediana": round(float(precos.median()), 2),
            "menor_preco": round(float(precos.min()), 2),
            "maior_preco": round(float(precos.max()), 2)
        }

        return estatisticas

    def comparar_precos_categorias(self):
        """Compara os preços médios das categorias de hardware."""

        resultados = []

        for categoria, df in self.bases.items():

            if "Price" not in df.columns:
                continue

            precos = df["Price"].dropna()

            if precos.empty:
                continue

            resultados.append({
                "categoria": categoria,
                "quantidade": len(precos),
                "preco_medio": round(float(precos.mean()), 2),
                "menor_preco": round(float(precos.min()), 2),
                "maior_preco": round(float(precos.max()), 2)
            })

        return pd.DataFrame(resultados).sort_values(
            by="preco_medio",
            ascending=False
        )

    def filtrar_produtos_por_preco(self, categoria, preco_minimo):
        """Filtra produtos de uma categoria pelo preço mínimo."""

        if categoria not in self.bases:
            raise ValueError("Categoria não encontrada.")

        df = self.bases[categoria]

        if "Price" not in df.columns:
            raise ValueError("Essa categoria não possui preços.")

        produtos = df[df["Price"] >= preco_minimo]

        return produtos[["Name", "Price"]].sort_values(
            by="Price",
            ascending=False
        )
