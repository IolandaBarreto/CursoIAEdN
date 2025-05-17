'''3 - Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
** Instale o modulo requests - pip install requests **
URL da API ViaCEP, passando o CEP informado
    url = f"https://viacep.com.br/ws/{cep}/json/"'''
    

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Verifica erros HTTP

        dados = resposta.json()

        if "erro" in dados:
            print("❌ CEP não encontrado.")
            return

        print("\n=== Endereço Encontrado ===")
        print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
        print(f"Bairro    : {dados.get('bairro', 'Não disponível')}")
        print(f"Cidade    : {dados.get('localidade', 'Não disponível')}")
        print(f"Estado    : {dados.get('uf', 'Não disponível')}")

    except requests.exceptions.RequestException as erro:
        print("Erro de conexão:", erro)
    except Exception as e:
        print("Erro inesperado:", e)

if __name__ == "__main__":
    cep = input("Digite o CEP (somente números): ").strip()
    if len(cep) == 8 and cep.isdigit():
        consultar_cep(cep)
    else:
        print("CEP inválido. Insira exatamente 8 dígitos.")

