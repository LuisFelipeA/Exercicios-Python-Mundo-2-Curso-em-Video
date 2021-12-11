#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
parar = 1
contador = 0
while parar != 0:
    n = int(input("Digite um valor ou 999 para parar: "))

    if n == 999:
        parar = 0
    else:
        soma = soma + n
        contador += 1

print(f"Foram digitados {contador} numeros e a soma entre eles é {soma}")