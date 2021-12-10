# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
 
 
soma_idade = 0
mais_velho = 0
mulher = 0

for i in range(1, 5):
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    idade = float(input(f"Digite o idade da {i}ª pessoa: "))
    sexo = input(f"Digite o sexo da {i}ª pessoa: F para feminino e M para masculino ").upper()
    soma_idade = soma_idade + idade

    if sexo == "M" and idade >= mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
    
    elif sexo == "F" and idade < 20:
        mulher += 1

media = soma_idade/4

print(f"A media de idade do grupo é {media:.1f} anos, o nome do homem mais velho é {nome_mais_velho} e tem {mulher} mulheres com menos de 20 anos")