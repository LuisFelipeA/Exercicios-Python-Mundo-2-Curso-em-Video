# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8

qtd = int(input("Digite quantos elementos da sequencia de fibonacci quer mostrar: "))

contador = 0
f = 0
f2 = 1

while contador < qtd:
    n = f + f2
    print (n, end=" > ")
    f = f2
    f2 = n
    contador += 1

print("Fim")