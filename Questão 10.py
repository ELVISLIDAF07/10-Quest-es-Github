# Solicitar ao usuário que insira seu nome
nome = input("Digite seu nome (maior que 3 caracteres): ")

# Validar o nome
while len(nome) <= 3:
    nome = input("Nome inválido. Digite um nome com mais de 3 caracteres: ")

# Solicitar ao usuário que insira sua idade
idade = int(input("Digite sua idade (entre 0 e 150): "))

# Validar a idade
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida. Digite uma idade entre 0 e 150: "))

# Solicitar ao usuário que insira seu salário
salario = float(input("Digite seu salário (maior que zero): "))

# Validar o salário
while salario <= 0:
    salario = float(input("Salário inválido. Digite um salário maior que zero: "))

# Solicitar ao usuário que insira seu sexo
sexo = input("Digite seu sexo ('f' para feminino ou 'm' para masculino): ")

# Validar o sexo
while sexo not in ['f', 'm']:
    sexo = input("Sexo inválido. Digite 'f' para feminino ou 'm' para masculino: ")

# Solicitar ao usuário que insira seu estado civil
estado_civil = input("Digite seu estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado): ")

# Validar o estado civil
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Estado civil inválido. Digite 's' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado: ")

# Imprimir as informações validadas
print("Informações validadas:")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {'Solteiro' if estado_civil == 's' else 'Casado' if estado_civil == 'c' else 'Viúvo' if estado_civil == 'v' else 'Divorciado'}")
