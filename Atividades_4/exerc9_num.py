'''9 - Solicite ao usuário números inteiros até que ele digite "0". Armazene os positivos e negativos separadamente em duas listas. Ignore valores não inteiros com try/except. No final, mostre quantos positivos e negativos foram inseridos.'''

# Listas para armazenar positivos e negativos
positivos = []
negativos = []

# Loop principal
while True:
    entrada = input("Digite um número inteiro (ou 0 para sair): ")

    try:
        numero = int(entrada)

        if numero == 0:
            break  # Encerra o programa

        if numero > 0:
            positivos.append(numero)
        else:
            negativos.append(numero)

    except ValueError:
        print("Valor inválido. Digite apenas números inteiros.")

# Exibe os resultados
print(f"\nTotal de números positivos: {len(positivos)}")
print(f"Total de números negativos: {len(negativos)}")