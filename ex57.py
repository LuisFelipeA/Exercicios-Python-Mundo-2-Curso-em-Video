#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 0

while sexo != "F" and sexo != "M":
    sexo = input("Digite o sexo: F/M: ").upper()

if sexo == "F":
    print("Sexo feminino")

else:
    print("Sexo Masculino")
