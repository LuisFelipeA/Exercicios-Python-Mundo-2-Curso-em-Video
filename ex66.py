# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = contador = 0
while True:
    n = int(input("Digite um numero ou digite [999] para parar: "))
    if n == 999:
        break
    soma = soma + n
    contador += 1

print(f"A soma dos {contador} numeros é {soma}")