#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = 0
n2 = 0
operacao = 0

while operacao != 5:
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    operacao = 0

    while operacao != 4 and operacao != 5:
        print("-=-"*5)
        operacao = int(input("""Digite:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa """))

        if operacao == 1:
            print(f"Soma de {n1} e {n2} é {n1+n2}")
        
        elif operacao == 2:
            print(f"Multiplicação de {n1} e {n2} é {n1*n2}")
        
        elif operacao == 3:
            if n1 >= n2:
                print(f"{n1} é o maior")
            else:
                print(f"{n2} é o maior")
        
        elif operacao == 4:
            print("Digite novos valores")

        elif operacao == 5:
            print("FIM")            
        
        else:
            print("Operação invalida. Digite novamente")


