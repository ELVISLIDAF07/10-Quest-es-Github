# Solicitar ao usuário que insira a altura em metros
altura = float(input("Digite a sua altura em metros: "))

# Calcular o peso ideal usando a fórmula
peso_ideal = (72.7 * altura) - 58

# Imprimir o peso ideal
print(f"O seu peso ideal é aproximadamente {peso_ideal:.2f} quilogramas.")
