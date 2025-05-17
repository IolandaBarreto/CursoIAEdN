'''2 - Crie um programa que solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando a estrutura de repetição for.'''

# Solicita um número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Usa a estrutura de repetição for para exibir a tabuada de 1 a 10
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
    