'''2 - Crie um programa em Python que solicite um número do usuário e informe se ele é par ou ímpar.'''

# Pede um número inteiro ao usuário
numero = int(input("Digite um número: "))

# Verifica se é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
    