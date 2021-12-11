# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    contador = 1
    n = int(input("Digite um numero positivo para ver a tabuada ou um numero negativo para sair: "))
    
    if n < 0:
        break
    
    print(f"Tabuada do {n}")
    
    while contador < 11:
        print(f"{n} x {contador} = {n*contador}")
        contador += 1
        
print("Tabuada encerrada")