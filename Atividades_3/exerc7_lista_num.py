'''7 - Crie um programa que percorre uma lista de números inteiros e imprime apenas os que são números primos. Use o for para iterar, if para a verificação e continue para pular os que não são primos.'''

# Lista de números inteiros
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Percorre a lista
for num in numeros:
    # Ignora os números menores que 2 (não são primos)
    if num < 2:
        continue

    # Verifica se o número é primo
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break  # Sai do loop se encontrar um divisor

    # Se não for primo, pula para o próximo número
    if not eh_primo:
        continue

    # Se for primo, imprime
    print(num)