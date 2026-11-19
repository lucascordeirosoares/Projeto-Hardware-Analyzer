from src.analisador import AnalisadorHardware


def exibir_menu():
    print("\n========== HARDWARE ANALYZER ==========")
    print("1 - Listar categorias disponíveis")
    print("2 - Consultar estatísticas de preços")
    print("3 - Comparar preços entre categorias")
    print("4 - Filtrar produtos por preço")
    print("5 - Gráfico de barras: preços por categoria")
    print("6 - Histograma: distribuição de preços")
    print("7 - Gráfico de dispersão: núcleos x preço")
    print("8 - Gráfico de linha: preços médios por categoria")
    print("0 - Sair")
    print("=======================================")


def localizar_categoria(analisador, categoria_digitada):
    """Localiza uma categoria sem diferenciar maiúsculas e minúsculas."""

    for nome in analisador.bases:
        if nome.lower() == categoria_digitada.lower():
            return nome

    raise ValueError("Categoria não encontrada.")


def main():
    analisador = AnalisadorHardware()

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                print("\nCategorias disponíveis:")

                for categoria in analisador.bases:
                    print(f"- {categoria}")

            elif opcao == 2:
                categoria_digitada = input("Digite a categoria: ").strip()
                categoria = localizar_categoria(analisador, categoria_digitada)

                estatisticas = analisador.obter_estatisticas_preco(categoria)

                if estatisticas is None:
                    print("Não existem preços disponíveis nessa categoria.")
                else:
                    print("\nEstatísticas de preços (USD):")

                    for chave, valor in estatisticas.items():
                        print(f"{chave}: {valor}")

            elif opcao == 3:
                comparacao = analisador.comparar_precos_categorias()

                print("\nComparação de preços médios (USD):")
                print(comparacao.to_string(index=False))

            elif opcao == 4:
                categoria_digitada = input("Digite a categoria: ").strip()
                categoria = localizar_categoria(analisador, categoria_digitada)

                preco_minimo = float(
                    input("Digite o preço mínimo em USD: ")
                )

                produtos = analisador.filtrar_produtos_por_preco(
                    categoria, preco_minimo
                )

                print(produtos.to_string(index=False))

            elif opcao == 5:
                analisador.grafico_precos_por_categoria()

            elif opcao == 6:
                categoria_digitada = input("Digite a categoria: ").strip()
                categoria = localizar_categoria(analisador, categoria_digitada)

                analisador.grafico_distribuicao_precos(categoria)

            elif opcao == 7:
                analisador.grafico_nucleos_preco_cpu()

            elif opcao == 8:
                analisador.grafico_linha_precos_categorias()

            elif opcao == 0:
                print("Encerrando o Hardware Analyzer...")
                break

            else:
                print("Opção inválida. Escolha uma opção do menu.")

        except ValueError as erro:
            print(f"Entrada inválida: {erro}")

        except Exception as erro:
            print(f"Ocorreu um erro: {erro}")


if __name__ == "__main__":
    main()