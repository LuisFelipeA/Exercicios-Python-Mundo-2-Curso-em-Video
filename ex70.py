# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

mais_mil = soma = barato = 0

while True:
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o preço: "))

    soma = soma + valor

    if valor > 1000:
        mais_mil += 1

    if barato == 0:
        nome_barato = nome
        barato = valor

    elif barato > valor:
        barato = valor
        nome_barato = nome

    continua = " "
    while continua not in "SN":
        continua = input("Deseja continuar? [S/N] ").upper()

    if continua == "N":
        break

print(f"Total gasto na compra: R${soma:.2f}")

print(f"Produtos que custam mais de R$1000: {mais_mil}")

print(f"Produto mais barato: {nome_barato}")