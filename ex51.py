#Desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

decimo = 10 * razao

for i in range(termo, decimo, razao):
    print(i, end=" > ")

print("Fim")