# Solicitar ao usuário que insira um número
numero = int(input("Digite um número de 1 a 7: "))

# Mapear o número para o dia da semana correspondente
if numero == 1:
    dia_semana = "Domingo"
elif numero == 2:
    dia_semana = "Segunda-feira"
elif numero == 3:
    dia_semana = "Terça-feira"
elif numero == 4:
    dia_semana = "Quarta-feira"
elif numero == 5:
    dia_semana = "Quinta-feira"
elif numero == 6:
    dia_semana = "Sexta-feira"
elif numero == 7:
    dia_semana = "Sábado"
else:
    dia_semana = "Valor Inválido"

# Imprimir o dia da semana correspondente ou "Valor Inválido"
print(f"O dia correspondente ao número {numero} é {dia_semana}.")
