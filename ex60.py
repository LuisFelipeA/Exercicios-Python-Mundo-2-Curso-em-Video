# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input("Digite um numero para saber o fatorial: "))
fatorial = 1
contador = n 
while contador != 1:
    fatorial = fatorial * contador
    contador = contador - 1

print(f"Fatorial de {n}! é {fatorial}")