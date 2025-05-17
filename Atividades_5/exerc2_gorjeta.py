'''2 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
A função deve receber dois parâmetros:
valor_conta (float): O valor total da conta
porcentagem_gorjeta (float): A porcentagem da gorjeta (por exemplo, 10 para 10%)'''


# Função para calcular o valor da gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

# Programa principal
try:
    conta = float(input("Digite o valor da conta (em R$): "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

    gorjeta = calcular_gorjeta(conta, porcentagem)
    total = conta + gorjeta

    print(f"\nValor da gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar (conta + gorjeta): R$ {total:.2f}")

except ValueError:
    print("Erro: Por favor, insira apenas números válidos.")
