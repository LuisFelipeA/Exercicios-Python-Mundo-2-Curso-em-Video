# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

maior_18 = 0
homem = mulher = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = " "
    while sexo not in "FM":
        sexo = input("Digite o sexo: [F/M] ").upper()

    if idade >= 18:
        maior_18 += 1
    
    if sexo == "M":
        homem += 1

    elif sexo == "F" and idade < 20:
        mulher += 1

    continua = " "
    while continua not in "SN":
        continua = input("Deseja continuar? [S/N] ").upper()

    if continua == "N":
        break

print(f"Pessoas com mais de 18 anos : {maior_18}")
print(f"Homens cadastrados: {homem}")
print(f"Mulheres com menos de 20 anos: {mulher}")