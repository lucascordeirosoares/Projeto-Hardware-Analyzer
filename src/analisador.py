
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    
    def grafico_precos_por_categoria(self):
        """Exibe um gráfico de barras com os preços médios por categoria."""

        comparacao = self.comparar_precos_categorias()

        if comparacao.empty:
            print("Não existem dados disponíveis para gerar o gráfico.")
            return

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=comparacao,
            x="categoria",
            y="preco_medio"
        )

        plt.title("Preço médio por categoria de hardware")
        plt.xlabel("Categoria")
        plt.ylabel("Preço médio (USD)")

        plt.tight_layout()
        plt.show()

    def grafico_distribuicao_precos(self, categoria):
        """Exibe um histograma com a distribuição dos preços."""

        if categoria not in self.bases:
            raise ValueError("Categoria não encontrada.")

        df = self.bases[categoria]

        if "Price" not in df.columns:
            raise ValueError("Essa categoria não possui preços.")

        precos = df["Price"].dropna()

        if precos.empty:
            print("Não existem preços disponíveis para essa categoria.")
            return

        plt.figure(figsize=(10, 6))

        sns.histplot(
            data=precos,
            bins=20,
            kde=True
        )

        plt.title(f"Distribuição dos preços - {categoria}")
        plt.xlabel("Preço (USD)")
        plt.ylabel("Quantidade de produtos")

        plt.tight_layout()
        plt.show()

    def grafico_nucleos_preco_cpu(self):
        """Exibe a relação entre núcleos e preços dos processadores."""

        df = self.bases["CPU"]

        dados = df[["Cores", "Price"]].copy()

        dados["Cores"] = pd.to_numeric(
            dados["Cores"], errors="coerce"
        )

        dados["Price"] = pd.to_numeric(
            dados["Price"], errors="coerce"
        )

        dados = dados.dropna()

        if dados.empty:
            print("Não existem dados suficientes para gerar o gráfico.")
            return

        plt.figure(figsize=(10, 6))

        sns.scatterplot(
            data=dados,
            x="Cores",
            y="Price"
        )

        plt.title("Relação entre núcleos e preço dos processadores")
        plt.xlabel("Quantidade de núcleos")
        plt.ylabel("Preço (USD)")

        plt.tight_layout()
        plt.show()

    
    def grafico_linha_precos_categorias(self):
        """Exibe um gráfico de linha com os preços médios por categoria."""

        comparacao = self.comparar_precos_categorias()

        if comparacao.empty:
            print("Não existem dados disponíveis para gerar o gráfico.")
            return

        plt.figure(figsize=(10, 6))

        plt.plot(
            comparacao["categoria"],
            comparacao["preco_medio"],
            marker="o"
        )

        plt.title("Preço médio por categoria de hardware")
        plt.xlabel("Categoria")
        plt.ylabel("Preço médio (USD)")

        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
