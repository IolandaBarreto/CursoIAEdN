'''3 - Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.'''


while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário quer sair do programa
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue
    
    # Verifica se a senha contém pelo menos um número
    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        print("Senha fraca: deve conter pelo menos um número.")
        continue
    
    # Se passou nas duas verificações, a senha é forte
    print("Senha válida e forte!")
    break