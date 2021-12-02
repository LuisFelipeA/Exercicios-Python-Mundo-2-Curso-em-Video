# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
#a<b+c

a = float(input("Digite a primeira reta"))
b = float(input("Digite a segunda reta"))
c = float(input("Digite a terceira reta"))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Triangulo Equilatero")

    elif a == b or b == c or a == c:
        print("Triangulo Isosceles")

    else:
        print("Triangulo Escaleno")

else:
    print("Nao é possivel formar um triangulo")