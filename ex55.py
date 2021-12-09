#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0 
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    if peso >= maior_peso:
        maior_peso = peso

    if peso <= menor_peso or menor_peso == 0:
        menor_peso = peso

print(f"O maior peso foi {maior_peso}Kg e o menor peso foi {menor_peso}Kg")