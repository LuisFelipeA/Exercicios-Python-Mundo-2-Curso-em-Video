#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
pares = 0

for i in range(6):
    n = int(input("Digite um numero inteiro: "))
    if n%2 == 0:
        soma = soma + n
        pares += 1

print(f"{pares} dos numeros digitados eram pares e a soma deles é {soma}")