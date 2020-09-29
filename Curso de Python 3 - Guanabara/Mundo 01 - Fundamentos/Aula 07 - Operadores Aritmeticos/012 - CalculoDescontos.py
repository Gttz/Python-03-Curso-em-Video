produto = float(input("Digite o preço do produto: "))

desconto = produto-(produto * 5/100)

print("O produto que custava R${:.2f} com o desconto de 5% agora custa {:.2f}".format(produto, desconto))
