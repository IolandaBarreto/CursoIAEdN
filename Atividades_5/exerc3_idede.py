'''3 - Crie uma função que calcule a idade de uma pessoa em dias, com base no ano de nascimento informado pelo usuário.
O programa deve considerar o ano atual como base para o cálculo.
Use try/except para tratar erros de entrada e valide que o ano não pode ser maior que o ano atual.'''


from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year  # Pega o ano atual
    if ano_nascimento > ano_atual:
        raise ValueError("O ano de nascimento não pode ser maior que o ano atual.")
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Considera anos com 365 dias (sem contar anos bissextos)
    return idade_dias

while True:
    try:
        ano = int(input("Digite seu ano de nascimento (ex: 1990): "))
        dias = calcular_idade_em_dias(ano)
        print(f"Sua idade em dias é aproximadamente: {dias} dias.")
        break  # Sai do loop se tudo der certo
    except ValueError as e:
        print(f"Erro: {e}. Tente novamente.")
