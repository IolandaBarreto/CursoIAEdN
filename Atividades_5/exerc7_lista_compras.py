'''7 - Crie um programa que permita ao usuário montar uma lista de compras. O usuário poderá adicionar itens até digitar "fim". Ao final, o programa exibirá todos os itens da lista. O programa deve estar estruturado com uma função main() e ser executado com if __name__ == "__main__":.'''


def main():
    lista_compras = []

    while True:
        item = input("Digite um item para a lista de compras (ou 'fim' para encerrar): ").strip()
        if item.lower() == "fim":
            break
        if item == "":
            print("Item vazio não será adicionado. Tente novamente.")
            continue
        lista_compras.append(item)

    print("\nItens da lista de compras:")
    for i, item in enumerate(lista_compras, start=1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
