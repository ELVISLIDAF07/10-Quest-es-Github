# Solicitar ao usuário que insira o preço dos três produtos
preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))

# Encontrar o produto mais barato usando a função min()
produto_mais_barato = min(preco_produto1, preco_produto2, preco_produto3)

# Imprimir a decisão
if produto_mais_barato == preco_produto1:
    print("Você deve comprar o primeiro produto.")
elif produto_mais_barato == preco_produto2:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")
