'''9 - Crie um programa onde o computador escolhe um número entre 1 e 10, e o usuário deve adivinhar qual é. O programa continua pedindo tentativas até que o usuário acerte. Use while, break e True para controlar o fluxo.'''

import random  # Importa o módulo para gerar números aleatórios

# Computador escolhe um número aleatório de 1 a 10
numero_secreto = random.randint(1, 10)

# Loop infinito até o usuário acertar
while True:
    # Pede um número ao usuário
    palpite = int(input("Tente adivinhar o número de 1 a 10: "))

    # Verifica se o palpite está certo
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break  # Sai do loop quando o usuário acerta
    else:
        print("Errado! Tente novamente.")
        
        