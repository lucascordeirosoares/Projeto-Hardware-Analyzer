
from src.analisador import AnalisadorHardware


def exibir_menu():
    print("\n========== HARDWARE ANALYZER ==========")
    print("1 - Listar categorias disponíveis")
    print("2 - Consultar estatísticas de preços")
    print("3 - Comparar preços entre categorias")
    print("4 - Filtrar produtos por preço")
    print("0 - Sair")
    print("=======================================")


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
                categoria = input("Digite a categoria: ").strip()
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
                categoria = input("Digite a categoria: ").strip().upper()
                preco_minimo = float(input("Digite o preço mínimo em USD: "))

                produtos = analisador.filtrar_produtos_por_preco(
                    categoria, preco_minimo
                )

                print(produtos.to_string(index=False))

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
