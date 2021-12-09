#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

p = input("Digite uma frase para saber se é palindromo: ").replace(" ","").upper()

pinverte = p[::-1]

if p == pinverte:
    print("É um palindromo")

else:
    print("Não é um palindromo")