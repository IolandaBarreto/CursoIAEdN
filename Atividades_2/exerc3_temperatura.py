'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

# Solicita a temperatura que será convertida
temperatura = float(input("Digite a temperatura: "))

# Solicita a unidade de origem (C, F ou K)
origem = input("Digite a unidade de origem (C, F ou K): ").upper()

# Solicita a unidade de destino (C, F ou K)
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Converte a temperatura com base nas unidades
resultado = None  # Valor inicial

if origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32  # Celsius para Fahrenheit
    elif destino == "K":
        resultado = temperatura + 273.15       # Celsius para Kelvin
    elif destino == "C":
        resultado = temperatura                # Mesma unidade

elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9   # Fahrenheit para Celsius
    elif destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15  # Fahrenheit para Kelvin
    elif destino == "F":
        resultado = temperatura                # Mesma unidade

elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15       # Kelvin para Celsius
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32  # Kelvin para Fahrenheit
    elif destino == "K":
        resultado = temperatura                # Mesma unidade

# Mostra o resultado ou mensagem de erro se as unidades forem inválidas
if resultado is not None:
    print(f"Temperatura convertida: {round(resultado, 2)} °{destino}")
else:
    print("Unidades inválidas. Use apenas C, F ou K.")