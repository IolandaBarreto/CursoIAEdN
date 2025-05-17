'''5 - Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), e mostre o resultado de acordo com a operação escolhida.
'''# Pede dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Pede a operação desejada
operacao = input("Digite a operação (+, -, * ou /): ")

# Verifica a operação e faz o cálculo
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida!"

# Mostra o resultado
print("Resultado:", resultado)