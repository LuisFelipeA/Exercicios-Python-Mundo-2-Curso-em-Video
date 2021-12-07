#Faça uma tabuada de um número que o usuário escolher, utilizando um laço for.

n = int(input("Digite um numero para ver a tabuada: "))

print(f"Tabuada do {n}")

for i in range(1, 11):

    print(f"{n} x {i} = {n*i}")
