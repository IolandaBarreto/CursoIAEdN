'''8- Calculadora Simples
Enunciado:
Crie um programa que simule uma calculadora simples. O usuário deve informar dois números e a operação desejada (+, -, *, /) e o programa deve exibir o resultado da operação.'''

# Solicita dois números ao usuário (podem ser inteiros ou decimais)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Verifica qual operação foi escolhida e calcula o resultado
if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == "/":
    # Verifica se o divisor é diferente de zero
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida. Use apenas +, -, * ou /.")
    