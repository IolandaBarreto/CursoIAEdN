'''4 - Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.'''


notas = []  # Lista para armazenar as notas válidas

while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
    
    if entrada.lower() == 'fim':
        break  # Sai do loop quando o professor digita 'fim'
    
    try:
        nota = float(entrada)  # Converte a entrada para número decimal
        
        # Verifica se a nota está entre 0 e 10
        if 0 <= nota <= 10:
            notas.append(nota)  # Adiciona nota válida na lista
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número ou 'fim' para sair.")

# Calcula e exibe a média da turma, se houver notas registradas
if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")