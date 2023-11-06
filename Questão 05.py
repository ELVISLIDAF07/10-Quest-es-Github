# Solicitar ao usuário que insira uma letra para representar o gênero
letra_genero = input("Digite 'F' para Feminino ou 'M' para Masculino: ")

# Verificar o gênero e imprimir a resposta correspondente
if letra_genero == 'F' or letra_genero == 'f':
    print("Feminino")
elif letra_genero == 'M' or letra_genero == 'm':
    print("Masculino")
else:
    print("Sexo Inválido")
