from src.analisador import AnalisadorHardware

analisador = AnalisadorHardware()

print("\nBases disponíveis:")
print(list(analisador.bases.keys()))