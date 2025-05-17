'''6 - Crie um programa que receba um número do usuário e diga se ele é positivo, negativo ou igual a zero.'''

# Pede um número ao usuário
numero = float(input("Digite um número: "))

# Verifica se é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")
    
