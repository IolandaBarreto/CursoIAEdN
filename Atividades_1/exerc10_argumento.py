'''10 - Crie uma função que receba um número como argumento e retorne o quadrado desse número. Depois, chame essa função passando um número digitado pelo usuário.'''

# Função que retorna o quadrado de um número
def quadrado(numero):
    return numero ** 2

# Pede um número ao usuário
numero_usuario = float(input("Digite um número: "))

# Chama a função e mostra o resultado
resultado = quadrado(numero_usuario)
print("O quadrado do número é:", resultado)
