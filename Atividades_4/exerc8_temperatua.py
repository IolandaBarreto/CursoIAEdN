''' - Crie um programa para registrar as temperaturas de vários dias. O usuário deve digitar a temperatura em graus Celsius (ex: 25.5). O programa continua coletando até que o usuário digite "fim" ou colete 7 temperaturas. Valores inválidos devem ser ignorados. Ao final, exiba a média das temperaturas registradas.'''

# Lista para armazenar as temperaturas válidas
temperaturas = []

# Loop até coletar 7 temperaturas ou até digitar 'fim'
while len(temperaturas) < 7:
    entrada = input(f"Digite a temperatura {len(temperaturas)+1} (ou 'fim' para encerrar): ")

    if entrada.lower() == "fim":
        break  # Encerra se o usuário digitar 'fim'

    try:
        # Tenta converter a entrada para float
        temp = float(entrada)
        temperaturas.append(temp)
    except ValueError:
        print("Valor inválido. Digite um número válido ou 'fim'.")

# Exibe a média, se houver pelo menos uma temperatura válida
if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"\nTemperaturas registradas: {temperaturas}")
    print(f"Média das temperaturas: {media:.2f}°C")
else:
    print("Nenhuma temperatura válida foi registrada.")