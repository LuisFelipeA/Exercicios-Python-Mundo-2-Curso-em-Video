#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print("""Jokenpô
    0-Papel
    1-Tesoura
    2-Pedra: """)
humano = int(input("Digite: "))

print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Pô")

print("=-"*20)

opcoes = ("Papel", "Tesoura", "Pedra")
pc = randint(0, 2) 

if pc == 0:
    if humano == 0:
        print(f"Computador jogou {opcoes[pc]}. Empatou!")
    if humano == 1:
        print(f"Computador jogou {opcoes[pc]}. Humano Vence!")
    if humano == 2:
        print(f"Computador jogou {opcoes[pc]}. Computador Vence!")

if pc == 1:
    if humano == 0:
        print(f"Computador jogou {opcoes[pc]}. Computador Vence!")
    if humano == 1:
        print(f"Computador jogou {opcoes[pc]}. Empatou!")
    if humano == 2:
        print(f"Computador jogou {opcoes[pc]}. Humano Vence!")

if pc == 2:
    if humano == 0:
        print(f"Computador jogou {opcoes[pc]}. Humano Vence!")
    if humano == 1:
        print(f"Computador jogou {opcoes[pc]}. Computador Vence!")
    if humano == 2:
        print(f"Computador jogou {opcoes[pc]}. Empatou!")

print("=-"*20)