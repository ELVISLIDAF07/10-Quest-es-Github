# Solicitar ao usuário que insira os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicitar ao usuário que escolha a operação
operacao = input("Escolha a operação a ser realizada (+, -, *, /): ")

# Verificar e realizar a operação escolhida
if operacao == "+":
    resultado = numero1 + numero2
    operacao_descricao = "soma"
elif operacao == "-":
    resultado = numero1 - numero2
    operacao_descricao = "subtração"
elif operacao == "*":
    resultado = numero1 * numero2
    operacao_descricao = "multiplicação"
elif operacao == "/":
    resultado = numero1 / numero2
    operacao_descricao = "divisão"
else:
    print("Operação inválida.")
    exit()

# Verificar se o resultado é par ou ímpar
par_ou_impar = "par" if resultado % 2 == 0 else "ímpar"

# Verificar se o resultado é positivo ou negativo
positivo_ou_negativo = "positivo" if resultado > 0 else "negativo"

# Verificar se o resultado é inteiro ou decimal
inteiro_ou_decimal = "inteiro" if resultado.is_integer() else "decimal"

# Imprimir o resultado e informações sobre os números
print(f"O resultado da {operacao_descricao} é: {resultado}")
print(f"O resultado é {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}.")
