#Desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão usando a estrutura while e pergunte para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.


termo = int(input("Digite o primeiro termo ou 0 para sair: "))
razao = int(input("Digite a razão: "))

contador_termo = 0
razao_soma = 0
qtd_termo = 10
add_termos = 0

while qtd_termo != 0:
    qtd_termo = qtd_termo + add_termos

    while contador_termo < qtd_termo:
        print(termo + razao_soma, end=" > ")
        razao_soma = razao_soma + razao
        contador_termo += 1

    add_termos = int(input("\nDigite quantos termos quer a mais ou 0 para sair: "))

    if add_termos == 0:
        qtd_termo = 0

print("Fim")