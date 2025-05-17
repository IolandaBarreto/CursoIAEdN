'''5 - Crie um programa que use um loop for para imprimir apenas os números ímpares de 1 a 10, pulando os pares com o comando continue.'''

# Loop que vai de 1 até 10
for numero in range(1, 11):
    # Se o número for par, pula para a próxima repetição
    if numero % 2 == 0:
        continue
    # Se for ímpar, imprime o número
    print(numero)
    
    
