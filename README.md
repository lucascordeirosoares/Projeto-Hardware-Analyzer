# Hardware Analyzer — Análise de Dados de Hardware com Python

**Disciplina:** Linguagem de Programação em Python (2026.2)  
**Professor:** Ruben Prado  
**Instituição:** Faculdade Senac-DF de Tecnologia e Inovação

---

## Sobre o projeto

O **Hardware Analyzer** é um sistema analítico interativo desenvolvido em Python para explorar e analisar dados de diferentes componentes de hardware.

O projeto utiliza uma base de dados real disponibilizada no Kaggle e permite consultar estatísticas de preços, comparar categorias de componentes, filtrar produtos e visualizar informações por meio de gráficos.

A aplicação funciona diretamente pelo terminal (CLI — Command Line Interface), utilizando Programação Orientada a Objetos para organizar a lógica de processamento e análise dos dados.

## Objetivos

- Analisar dados de diferentes categorias de hardware.
- Calcular estatísticas de preços, como média, mediana, menor e maior valor.
- Comparar os preços médios entre categorias.
- Filtrar produtos de acordo com um preço mínimo.
- Apresentar visualizações que facilitem a interpretação dos dados.

## Fonte de dados

- **Tema geral:** Tecnologia e componentes de hardware.
- **Dataset:** General Computer Hardware Dataset.
- **Autor:** Dilshaan Sandhu.
- **Fonte:** [Kaggle — General Computer Hardware Dataset](https://www.kaggle.com/datasets/dilshaansandhu/general-computer-hardware-dataset)
- **Moeda dos preços:** Dólar americano (USD).

A base reúne informações sobre diferentes componentes de computadores, incluindo processadores, placas de vídeo, memórias RAM, SSDs, HDs, monitores, placas-mãe, fontes, gabinetes e coolers.

A escolha desse conjunto de dados foi motivada pelo interesse em tecnologia e hardware. O objetivo é analisar os valores registrados na base, comparar os preços médios entre as categorias e identificar padrões e diferenças nos valores dos componentes.

**Observação:** os preços representam os registros disponíveis no dataset e não necessariamente correspondem aos preços atuais praticados no mercado.

## Estrutura do projeto

```text
Projeto-Hardware-Analyzer/
│
├── data/
│   ├── CPUData.csv
│   ├── GPUData.csv
│   ├── RAMData.csv
│   ├── SSDData.csv
│   ├── HDDData.csv
│   ├── MonitorData.csv
│   ├── MotherboardData.csv
│   ├── PSUData.csv
│   ├── CaseData.csv
│   └── CPUCoolerData.csv
│
├── src/
│   ├── __init__.py
│   └── analisador.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Pandas:** leitura, limpeza, organização e análise dos dados.
- **Matplotlib:** criação dos gráficos.
- **Seaborn:** construção de visualizações estatísticas.

## Arquitetura e implementação

### Classe AnalisadorHardware

A classe `AnalisadorHardware`, localizada em `src/analisador.py`, concentra a lógica principal do sistema.

Suas responsabilidades incluem:

- Carregar automaticamente os arquivos CSV presentes na pasta `data/`.
- Organizar os dados em categorias de hardware.
- Realizar a limpeza e preparação dos dados.
- Calcular estatísticas de preços.
- Comparar os preços entre categorias.
- Filtrar produtos por preço mínimo.
- Gerar os gráficos analíticos.

O arquivo `main.py` é responsável pelo menu interativo e pela comunicação com os métodos da classe, mantendo a separação entre a interface do usuário e a lógica de processamento.

### Limpeza e preparação dos dados

Durante o carregamento das bases, foram aplicadas técnicas de tratamento utilizando Pandas:

- Remoção de registros duplicados com `drop_duplicates()`.
- Remoção de produtos sem nome utilizando `dropna()`.
- Remoção de espaços extras dos campos textuais com `str.strip()`.
- Substituição de textos vazios por valores ausentes.
- Conversão dos preços para valores numéricos com `pd.to_numeric()`.
- Preenchimento de informações textuais ausentes com `fillna()`.

Os valores de preço ausentes foram preservados como valores nulos para não comprometer os cálculos estatísticos.

## Funcionalidades do sistema

O menu interativo disponibiliza as seguintes opções:

1. Listar categorias disponíveis.
2. Consultar estatísticas de preços de uma categoria.
3. Comparar preços entre categorias.
4. Filtrar produtos por preço mínimo.
5. Gerar gráfico de barras dos preços médios por categoria.
6. Gerar histograma da distribuição de preços.
7. Gerar gráfico de dispersão entre quantidade de núcleos e preço dos processadores.
8. Gerar gráfico de linha dos preços médios por categoria.
0. Encerrar o programa.

## Gráficos desenvolvidos

### 1. Gráfico de barras — Preço médio por categoria

Apresenta uma comparação dos preços médios dos componentes de hardware, permitindo identificar quais categorias possuem os maiores valores médios.

### 2. Histograma — Distribuição dos preços

Apresenta a distribuição dos preços dos produtos de uma categoria selecionada, permitindo observar a concentração e a variação dos valores registrados.

### 3. Gráfico de dispersão — Núcleos x preço dos processadores

Demonstra a relação entre a quantidade de núcleos dos processadores e seus preços, permitindo observar como essas duas características se distribuem na base de dados.

### 4. Gráfico de linha — Preço médio por categoria

Apresenta os preços médios das categorias de hardware em um gráfico de linha, facilitando a comparação visual dos valores registrados.

## Instalação e execução

### Pré-requisitos

- Python instalado.
- Git instalado (opcional, para clonar o repositório).

### 1. Clonar o repositório

```bash
git clone https://github.com/lucascordeirosoares/Projeto-Hardware-Analyzer.git
```

### 2. Entrar na pasta do projeto

```bash
cd Projeto-Hardware-Analyzer
```

### 3. Criar e ativar o ambiente virtual

Recomendado para isolar as dependências do projeto.

No Windows, utilizando PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o sistema

```bash
python main.py
```

## Considerações finais

O desenvolvimento do Hardware Analyzer proporcionou a aplicação prática de conceitos de programação em Python, manipulação de dados com Pandas, Programação Orientada a Objetos e visualização de informações.

O projeto demonstra como dados de produtos de hardware podem ser organizados, processados e transformados em informações úteis para análise e comparação de preços.

---

# 📝 Formulário Oficial de Entrega

### 👥 Integrantes da equipe

- Lucas Cordeiro Soares — 62088736
- Maria Heloísa Saturnina do Santos Silva — 62596556
- Kaylla Kristiny Nascimento de Macedo — 52173866
- Saulo Rodrigues Costa Filho — 62256796

 
