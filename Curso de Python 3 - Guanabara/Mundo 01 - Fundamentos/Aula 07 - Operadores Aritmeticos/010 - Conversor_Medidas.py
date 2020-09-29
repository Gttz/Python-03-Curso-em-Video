reais = float(input("Digite a quantidade em reais: R$"))

dólar = reais / 4.02

print("Com R${:.2f} você pode comprar US${:.2f}".format(reais, dólar))
