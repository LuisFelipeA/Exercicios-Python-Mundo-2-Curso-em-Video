# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

#Escolher 0 ou 1 aleatoriamente, onde 0 = par e 1 = impar


vitorias = 0
print("-----Par ou Impar-----")
while True:
    pc_n = randint(0, 11)
    pc_par_impar = randint(0,1)

    print("-"*15)


    player = int(input("Digite um numero: "))
    player_par_impar = input("[P]Par ou [I]Impar: ").upper()

    print("-"*15)


    if pc_par_impar == 0:
        print(f"Computador escolheu Par e o numero {pc_n}")
    else:
        print(f"Computador escolheu Impar e o numero {pc_n}")

    soma = player + pc_n
    resultado = soma%2

    if resultado == 0:
        if player_par_impar == "P":
            if pc_par_impar == 0:
                print("Empate")
            else:
                print("Jogador ganhou")
                vitorias += 1
        
        else:
            if  player_par_impar == "I":
                if pc_par_impar == 1:
                    print("Empate")
                else:
                    print("Computador ganhou")
                    break

    else:
        if player_par_impar == "I":
            if pc_par_impar == 1:
                print("Empate")
            else:
                print("Jogador ganhou")
                vitorias += 1
        else:
            if pc_par_impar == 0:
                print("Empate")
            else:
                print("Computador ganhou")
                break

    

print("-"*15)
print(f"Numero de vitorias consecutivas: {vitorias} vitoria(s)")
print("-"*15)
