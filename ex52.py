#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um numero para saber se ele é primo: "))

contador = 0
print("Divisivel por:")

for i in range(1, n+1):
    primo = n%i
    if primo == 0:
        print(i, end=" > ")
        contador += 1



if contador == 2:
    print(f"\nO numero {n} é divisivel apenas por 1 e {n}, então é um numero primo")
else:
    print(f"\nO numero {n} é divisivel por {contador} numeros diferentes, então não é primo")