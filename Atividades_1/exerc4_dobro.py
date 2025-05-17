'''4 - Crie uma função em Python que receba um número como parâmetro e retorne o dobro desse número. Depois, chame essa função com um número fornecido pelo usuário.'''

# Define a função que retorna o dobro do número
def dobro(numero):
    return numero * 2

# Pede um número ao usuário
numero_usuario = int(input("Digite um número: "))

# Chama a função e mostra o resultado
resultado = dobro(numero_usuario)
print("O dobro do número é:", resultado)
