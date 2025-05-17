'''8 - Crie um programa que armazene nomes de países e suas capitais em um dicionário. O usuário digita o nome do país e o programa mostra a capital correspondente.'''

# Dicionário com países e suas capitais
paises_capitais = {
    "Brasil": "Brasília",
    "Espanha": "Madri",
    "França": "Paris",
    "Alemanha": "Berlim",
    "Japão": "Tóquio"
}

# Pede o nome do país ao usuário
pais = input("Digite o nome de um país: ")

# Verifica se o país está no dicionário e mostra a capital
if pais in paises_capitais:
    print("A capital de", pais, "é", paises_capitais[pais])
else:
    print("País não encontrado.")
    