# Definindo os preços das carnes
precos = {
    "File Duplo": {"até 5 Kg": 4.90, "acima de 5 Kg": 5.80},
    "Alcatra": {"até 5 Kg": 5.90, "acima de 5 Kg": 6.80},
    "Picanha": {"até 5 Kg": 6.90, "acima de 5 Kg": 7.80}
}

# Solicitar ao usuário que escolha o tipo de carne e a quantidade
tipo_carne = input("Escolha o tipo de carne (File Duplo, Alcatra, ou Picanha): ")
quantidade = float(input("Digite a quantidade em Kg: "))

# Solicitar ao usuário que escolha o tipo de pagamento
tipo_pagamento = input("Escolha o tipo de pagamento (dinheiro ou cartão Tabajara): ")

# Calcular o preço total
if quantidade <= 5:
    preco_total = quantidade * precos[tipo_carne]["até 5 Kg"]
else:
    preco_total = quantidade * precos[tipo_carne]["acima de 5 Kg"]

# Calcular o desconto se o pagamento for com cartão Tabajara
desconto = 0
if tipo_pagamento.lower() == "cartão tabajara":
    desconto = preco_total * 0.05

# Calcular o valor a pagar
valor_a_pagar = preco_total - desconto

# Imprimir o cupom fiscal
print("CUPOM FISCAL")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade de carne: {quantidade:.2f} Kg")
print(f"Preço total: R${preco_total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Valor do desconto: R${desconto:.2f}")
print(f"Valor a pagar: R${valor_a_pagar:.2f}")
