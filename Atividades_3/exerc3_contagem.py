'''3 - Crie um programa que faça uma contagem regressiva a partir de um número informado pelo usuário até 0. O programa deve mostrar cada número da contagem e, ao final, exibir "FIM!".'''


# Solicita um número inteiro ao usuário
numero = int(input("Digite um número para a contagem regressiva: "))

# Faz a contagem regressiva do número até 0
for i in range(numero, -1, -1):
    print(i)

# Exibe a mensagem final
print("FIM!")