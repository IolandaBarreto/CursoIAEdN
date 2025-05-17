'''5 - Crie um programa com uma função que cadastre alunos e suas respectivas notas.
O sistema deve:
Solicitar o nome do aluno.
Solicitar 3 notas válidas (entre 0 e 10).
Armazenar os dados em um dicionário, onde a chave é o nome e o valor é uma lista de notas.
Permitir o cadastro de vários alunos até que o usuário digite "fim".
Exibir ao final:
A lista de alunos e suas médias.
O aluno com a maior média.
Use def para as funcionalidades e try/except para tratar entradas inválidas.'''

def cadastrar_aluno():
    """Função para cadastrar um aluno e suas 3 notas válidas."""
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()
    if nome.lower() == "fim":
        return None, None
    
    notas = []
    while len(notas) < 3:
        try:
            nota = float(input(f"Digite a nota {len(notas)+1} para {nome} (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
    return nome, notas

def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas)

def main():
    alunos = {}  # Dicionário para armazenar nome e lista de notas
    
    while True:
        nome, notas = cadastrar_aluno()
        if nome is None:  # Usuário digitou 'fim'
            break
        alunos[nome] = notas
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nLista de alunos e suas médias:")
    maior_media = -1
    aluno_maior_media = ""
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"{nome}: média {media:.2f}")
        if media > maior_media:
            maior_media = media
            aluno_maior_media = nome
    
    print(f"\nAluno com maior média: {aluno_maior_media} ({maior_media:.2f})")

# Executa o programa principal
main()


