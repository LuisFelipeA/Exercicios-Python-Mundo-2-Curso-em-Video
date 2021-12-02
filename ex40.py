#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))

media = (nota1+nota2)/2

if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0:
    print("Nota invalida. Digite novamente!")

else:
    if media >= 7:
        print(f"Media igual a {media:.1f}. Aluno aprovado!")

    elif media < 5:
        print(f"Media igual a {media:.1f}. Aluno Reprovado!")

    elif media >= 5 and media < 7:
        print(f"Media igual a {media:.1f}. Aluno de Recuperação!")

    else: 
        print("Nota invalida. Digite novamente!")