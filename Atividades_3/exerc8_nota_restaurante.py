'''8 - Crie um programa que solicita a nota de avaliação de um restaurante (de 0 a 5) e exibe a quantidade de estrelas equivalente, juntamente com uma mensagem personalizada. Use if, elif e else para lidar com diferentes faixas de nota.'''


# Solicita a nota ao usuário
nota = int(input("Dê uma nota para o restaurante (0 a 5): "))

# Verifica e exibe a avaliação com estrelas e mensagem
if nota == 5:
    print("★★★★★ - Excelente! Muito obrigado pela sua avaliação!")
elif nota == 4:
    print("★★★★ - Ótimo! Ficamos felizes que tenha gostado.")
elif nota == 3:
    print("★★★ - Bom! Vamos tentar melhorar ainda mais.")
elif nota == 2:
    print("★★ - Regular. Agradecemos o feedback.")
elif nota == 1:
    print("★ - Ruim. Sentimos muito, vamos melhorar.")
elif nota == 0:
    print("Sem estrelas - Lamentamos pela experiência. Vamos trabalhar para melhorar.")
else:
    print("Nota inválida. Por favor, digite um número de 0 a 5.")
    