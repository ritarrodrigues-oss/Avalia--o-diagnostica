# peça o valor de uma compra e aplique um descontode 10% se for acima de R$ 100,00.

valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Desconto de 10% aplicado. Valor final: R$ {valor_final:.2f}")
    