'''4 - Crie um programa que continue pedindo uma senha ao usuário até que ele digite a senha correta. Quando a senha correta for digitada, o programa mostra uma mensagem de sucesso e interrompe o loop com break.'''


# Define a senha correta
senha_correta = "1234"

# Loop que continua até a senha correta ser digitada
while True:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso liberado!")
        break  # Encerra o loop se a senha estiver correta
    else:
        print("Senha incorreta. Tente novamente.")
        
        