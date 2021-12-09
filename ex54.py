#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0
data_atual = date.today()

ano_atual = data_atual.year


for i in range(1,8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior += 1

    elif idade < 18 and idade > 0:
        menor += 1
    
    else:
        print("Data invalida")


print(f"Pessoas que ainda não atingiram a maioridade: {menor}. Quantas já são maiores: {maior}")