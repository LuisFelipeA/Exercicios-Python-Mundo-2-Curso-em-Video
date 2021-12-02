# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros

produto = float(input("Digite o valor do produto: "))
tipo_compra = int(input("""Pagamento: 
    Digite 1: a vista (dinheiro ou cheque)
    Digite 2: a vista (cartão)
    Digite 3: em até 2x no cartão
    Digite 4: 3x ou mais no cartão: """))

if tipo_compra == 1:
    print(f"Valor a pagar: R${produto-(produto*0.1):.2f}")

elif tipo_compra == 2:
    print(f"Valor a pagar: R${produto-(produto*0.05):.2f}")

elif tipo_compra == 3:
    print(f"Valor: 2 parcelas de R${produto/2:.2f}")

elif tipo_compra == 4:
    qtd_parcela = int(input("Quantidade de parcelas: "))
    valor = produto+(produto*0.2)
    print(f"Valor: {qtd_parcela} de R${valor/qtd_parcela:.2f}")

else:
    print("Opção invalida")