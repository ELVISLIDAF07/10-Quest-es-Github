# Solicitar ao usuário que insira a temperatura em graus Fahrenheit
temp_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Realizar a conversão para graus Celsius
temp_celsius = (5 * (temp_fahrenheit - 32)) / 9

# Imprimir o resultado
print(f"A temperatura em graus Celsius é: {temp_celsius:.2f}°C")
