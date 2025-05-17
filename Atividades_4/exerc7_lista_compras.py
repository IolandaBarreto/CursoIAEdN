'''7 - Crie um programa que permita que o usuário monte uma lista de compras digitando nomes de produtos. O usuário pode digitar até 10 itens. Se digitar "fim", o programa para imediatamente (break). Se o item for vazio (só apertar Enter), ele é ignorado com continue. Use try/except para garantir que apenas strings sejam inseridas.'''


# Lista para armazenar os produtos
lista_compras = []

# Loop que permite até 10 itens
for i in range(10):
    try:
        # Solicita o nome do produto
        produto = input(f"Digite o nome do produto {i + 1} (ou 'fim' para encerrar): ")

        # Se digitar 'fim', encerra o programa
        if produto.lower() == "fim":
            break

        # Se digitar vazio (só apertar Enter), ignora e continua
        if produto.strip() == "":
            print("Entrada vazia. Ignorando...")
            continue

        # Adiciona o produto à lista
        lista_compras.append(produto)

    except Exception:
        print("Erro ao ler a entrada. Tente novamente.")

# Exibe a lista final
print("\nLista de Compras:")
for item in lista_compras:
    print("- " + item)
    
