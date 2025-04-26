# Algoritmo de busca
def busca (lista, nome_procurado):
    for i in range(len(lista)):
        if lista[i ] == nome_procurado:
            return i + 1 # retorna para a posição
    return -1 # não encontrou
nomes = ["Maria", "Ana", "João", "Pedro"] 
posição = busca(nomes, "Ana")
nome_procurado = input ("Qual nome você quer procurar? ")
print("Ana está na posição:", posição)

# Algoritmo de busca - binária
def binaria (lista, valor_procurado):
    inicio = 0
    fim = len(lista) -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista [meio] == valor_procurado:
            inicio = meio + 1


