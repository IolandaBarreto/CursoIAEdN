'''4 - Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
** Instale o modulo requests - pip install requests **
URL da API com base na moeda informada
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"'''
    
import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Verifica erros HTTP
        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("❌ Moeda não encontrada ou código inválido.")
            return

        cotacao = dados[chave]

        print(f"\n=== Cotação de {moeda} para BRL ===")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Valor máximo: R$ {cotacao['high']}")
        print(f"Valor mínimo: R$ {cotacao['low']}")
        print(f"Data e hora da última atualização: {cotacao['create_date']}")

    except requests.exceptions.RequestException as erro:
        print("Erro de conexão:", erro)
    except Exception as e:
        print("Erro inesperado:", e)

if __name__ == "__main__":
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    if moeda.isalpha() and len(moeda) == 3:
        consultar_cotacao(moeda)
    else:
        print("Código de moeda inválido. Use 3 letras, como USD.")

