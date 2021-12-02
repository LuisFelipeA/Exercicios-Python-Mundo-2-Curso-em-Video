# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input("Digite o ano que nasceu: "))
idade = 2021-ano

if idade < 18:
    print(f"Voce tem {idade} anos, ainda não pode se alistar ao serviço militar.")

elif idade == 18:
    print(f"Voce tem {idade} anos, essa é a hora para se alistar ao serviço militar.")

else:
    print(f"Voce tem {idade} anos, ja passou do tempo para se alistar ao serviço militar.")
