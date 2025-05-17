'''5- Verificador de Número Primo
Enunciado:
Crie um programa que solicite um número inteiro positivo ao usuário e verifique se ele é um número primo. Um número primo só é divisível por 1 e por ele mesmo.'''


# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é menor que 2 (0 e 1 não são primos)
if numero < 2:
    print(numero, "não é um número primo.")
else:
    # Assume que o número é primo
    primo = True

    # Verifica se existe algum divisor além de 1 e ele mesmo
    for i in range(2, numero):
        if numero % i == 0:
            primo = False  # Encontrou um divisor
            break          # Sai do laço, já sabemos que não é primo

    # Exibe o resultado
    if primo:
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")
        
        