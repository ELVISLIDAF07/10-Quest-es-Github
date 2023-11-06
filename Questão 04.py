# Solicitar ao usuário que insira o valor do salário por hora e o número de horas trabalhadas no mês
valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcular o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcular os descontos
ir_desconto = 0.11 * salario_bruto
inss_desconto = 0.08 * salario_bruto
sindicato_desconto = 0.05 * salario_bruto

# Calcular o salário líquido
salario_liquido = salario_bruto - (ir_desconto + inss_desconto + sindicato_desconto)

# Imprimir os resultados
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"IR (11%): R${ir_desconto:.2f}")
print(f"INSS (8%): R${inss_desconto:.2f}")
print(f"Sindicato (5%): R${sindicato_desconto:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
