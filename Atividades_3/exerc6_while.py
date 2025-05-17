'''6 - Crie um programa que simula a validação de uma senha usando um loop while True. O usuário tem no máximo 3 tentativas para acertar a senha correta. Use break para encerrar o loop quando a senha for correta ou quando o número máximo de tentativas for atingido.'''

# Define a senha correta
senha_correta = "1234"

# Contador de tentativas
tentativas = 0

# Loop que permite até 3 tentativas
while True:
    senha = input("Digite a senha: ")
    tentativas += 1  # Conta a tentativa

    if senha == senha_correta:
        print("Acesso liberado!")
        break  # Sai do loop se a senha estiver correta
    else:
        print("Senha incorreta.")

    if tentativas == 3:
        print("Número máximo de tentativas atingido. Acesso bloqueado.")
        break  # Sai do loop após 3 tentativas