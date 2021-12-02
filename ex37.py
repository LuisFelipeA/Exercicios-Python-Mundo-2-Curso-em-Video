#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input("Digite um numero inteiro: "))
selecao = int(input("Digite 1 para binário, 2 para octal e 3 para hexadecimal: "))

bin = format(n, "b")
oct = format(n, "o")
hex = format(n, "x")


if selecao == 1:
    print(f"O numero {n} em binario é {bin}")

elif selecao == 2:
    print(f"O numero {n} em octal é {oct}")

elif selecao == 3:
    print(f"O numero {n} em hexadecimal é {hex}")

else:
    print("Digite novamente!!")