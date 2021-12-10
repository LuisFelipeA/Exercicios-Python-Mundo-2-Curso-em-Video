#Desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão usando a estrutura while.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

contador_termo = 0
razao_soma = 0

while contador_termo < 10:
    print(termo + razao_soma, end=" > ")
    razao_soma = razao_soma + razao
    contador_termo += 1

print("Fim")