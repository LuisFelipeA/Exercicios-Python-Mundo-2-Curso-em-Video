#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

sacar = int(input("Digite o valor para ser sacado: "))
restante = sacar
nota = 50
total_notas = 0

while True:
    if restante >= nota:
        restante = restante - nota
        total_notas += 1
    
    else:
        if total_notas > 0:
            print(f"Total de {total_notas} notas de R${nota}")
        
        if nota == 50:
            nota = 20
        
        elif nota == 20:
            nota = 10
        
        elif nota == 10:
            nota = 1
        
        total_notas = 0

        if restante == 0:
            break

            
