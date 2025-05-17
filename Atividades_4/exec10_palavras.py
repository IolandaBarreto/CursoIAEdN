'''10 - Peça ao usuário para digitar palavras. Armazene apenas as palavras com mais de 5 letras em uma lista. Se a palavra for "parar", o programa encerra (break). Se a palavra for numérica (como "123"), ignore com continue. Use try/except para garantir que só palavras (strings) sejam processadas. No final, exiba a lista das palavras longas inseridas.'''


palavras_longas = []

while True:
    entrada = input("Digite uma palavra (ou 'parar' para encerrar): ")

    try:
        # Verifica se o usuário quer encerrar
        if entrada.lower() == "parar":
            break

        # Ignora entradas numéricas
        if entrada.isnumeric():
            continue

        # Armazena apenas palavras com mais de 5 letras
        if len(entrada) > 5:
            palavras_longas.append(entrada)

    except Exception as e:
        print(f"Erro ao processar a entrada: {e}")
        continue

# Exibe as palavras longas inseridas
print("\nPalavras com mais de 5 letras inseridas:")
for palavra in palavras_longas:
    print("-", palavra)
