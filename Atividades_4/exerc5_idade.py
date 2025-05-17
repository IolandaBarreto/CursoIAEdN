'''5 - Crie um programa que solicite ao usuário a idade de várias pessoas. Armazene apenas idades válidas (entre 0 e 120) em uma lista. Use for, try/except, continue para ignorar entradas inválidas, e break para encerrar o programa se o usuário digitar "fim". No final, exiba a lista das idades válidas.'''


idades = []  # Lista para guardar as idades válidas

for _ in range(1000):  # Um limite alto para permitir várias entradas
    entrada = input("Digite a idade (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break  # Encerra o programa

    try:
        idade = int(entrada)  # Tenta converter a entrada para número inteiro

        # Verifica se a idade está no intervalo válido
        if 0 <= idade <= 120:
            idades.append(idade)  # Adiciona idade válida à lista
        else:
            print("Idade inválida! Deve estar entre 0 e 120.")
            continue  # Volta para o próximo laço
    except ValueError:
        print("Entrada inválida! Digite um número inteiro ou 'fim'.")
        continue

# Exibe a lista de idades válidas
print("Idades válidas registradas:", idades)
