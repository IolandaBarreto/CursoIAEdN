'''7- Verificador de Palíndromo
Enunciado:
Crie um programa que solicite uma palavra e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).'''


# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Converte a palavra para minúsculas para facilitar a comparação
palavra = palavra.lower()

# Inverte a palavra usando fatiamento [::-1]
palavra_invertida = palavra[::-1]

# Verifica se a palavra é igual à sua forma invertida
if palavra == palavra_invertida:
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')
    