'''while True:
    try:
        # Solicita o primeiro número
        num1 = float(input("Digite o primeiro número: "))
        
        # Solicita o segundo número
        num2 = float(input("Digite o segundo número: "))
        
        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ")
        
        # Verifica a operação e realiza o cálculo
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Use +, -, * ou /.")

        # Exibe o resultado e encerra o programa
        print(f"Resultado: {resultado}")
        break  # Sai do loop após operação bem-sucedida

    except ValueError as ve:
        print(f"Erro: {ve}. Tente novamente.")

    except ZeroDivisionError as ze:
        print(f"Erro: {ze}. Tente novamente.")'''
       
while True:
    try:
        # Solicita o primeiro número ao usuário e converte para float
        num1 = float(input("Digite o primeiro número: "))
        
        # Solicita o segundo número ao usuário e converte para float
        num2 = float(input("Digite o segundo número: "))
        
        # Solicita a operação desejada ao usuário
        operacao = input("Digite a operação (+, -, *, /): ")
        
        # Verifica qual operação o usuário escolheu e realiza o cálculo
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            # Verifica se o segundo número é zero para evitar divisão por zero
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            # Caso a operação digitada seja inválida, levanta um erro
            raise ValueError("Operação inválida. Use +, -, * ou /.")

        # Exibe o resultado da operação e encerra o programa
        print(f"Resultado: {resultado}")
        break  # Sai do loop quando a operação foi realizada com sucesso

    except ValueError as ve:
        # Captura erros de entrada inválida e operação inválida
        print(f"Erro: {ve}. Tente novamente.")

    except ZeroDivisionError as ze:
        # Captura erro de divisão por zero
        print(f"Erro: {ze}. Tente novamente.")        
        
