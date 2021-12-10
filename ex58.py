# O computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
import random

pc = random.randint(0,10)

user = "x"
tentativas = 1


while user != pc:
    user = int(input("Tente adivinhar o numero gerado pelo computador entre 0 e 10: "))
    
    if user >= 0 and user <= 10:
        if user > pc:
            print("O numero é menor")
            tentativas += 1
            
        elif user < pc:
            print("O numero é maior")
            tentativas += 1

        else:
            print("Acertou")
    else:
        print("Numero invalido")

print(f"Numero de tentativas: {tentativas}")
