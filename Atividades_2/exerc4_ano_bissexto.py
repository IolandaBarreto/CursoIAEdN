'''4- Verificador de Ano Bissexto
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.'''

# Solicita ao usuário que digite um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto usando as regras:
# - É divisível por 4
# - NÃO é divisível por 100, a menos que seja divisível por 400
if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")