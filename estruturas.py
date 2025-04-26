# Estrutura sequencial
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Cidade onde mora: ")
print("Olá", nome)
print("Você tem", idade, "anos")
print("E mora em", cidade)

#Estrutura de repetição
for i in range(5):
    print("Contar", i)

contar = 0
while contar < 5:
    print("Executar", contar)
    contar += 1
  
# Estrutura condicional
idade = 18
if idade > 18:
    print("Maior de idade!")
elif idade < 18:
    print("Menor de idade, vá dormir:")
else:
    print("Sei lá o que você é.")

ida = int(input("Digite a sua idade: "))
if ida >= 18:
    print("Maior de idade!")
elif idade < 18:
      print("Menor de idade")
else:
    print("Menor de idade!")
