# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


media = maior = menor = contador = soma = 0
continuar = "S"


while continuar == "S":

    n = int(input("Digite um numero: "))

    soma = soma + n
    contador += 1
    
    if menor == 0:
        menor = n

    elif n >= maior:
        maior = n
    
    elif n <= menor:
        menor = n

    continuar = input(f"Deseja continuar: S/N: ").upper()
    
media = soma/contador

print(f"A media dos numeros foi {media}")
print(f"O maior numero foi {maior} e o menor foi {menor}")