#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Valor da casa: "))
salario = float(input("Seu salario: "))
anos = int(input("Anos para pagar: "))

parcela = casa/anos/12
valor_parcela_aprovada = salario*0.3  

if parcela >= valor_parcela_aprovada:
    print("Emprestimo negado. Valor da parcela muito alto!!")

else:
    print("Emprestimo aprovado!!")
