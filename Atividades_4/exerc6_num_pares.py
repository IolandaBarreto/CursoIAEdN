'''6 - Peça ao usuário que digite 10 números inteiros. Armazene apenas os números pares válidos em uma lista. Use try/except para capturar erros, continue para ignorar números ímpares ou inválidos, e exiba a lista final ao terminar.'''

pares = []  # Lista para armazenar os números pares válidos
contador = 0  # Contador de tentativas

while contador < 10:
    entrada = input(f"Digite o {contador + 1}º número inteiro: ")

    try:
        numero = int(entrada)  # Tenta converter a entrada para inteiro

        if numero % 2 == 0:
            pares.append(numero)  # Adiciona se for par
        else:
            print("Número ímpar ignorado.")
            continue  # Pula para a próxima entrada
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        continue  # Pula para a próxima entrada

    contador += 1  # Só conta tentativas válidas

# Exibe a lista final de números pares válidos
print("Números pares válidos digitados:", pares)

