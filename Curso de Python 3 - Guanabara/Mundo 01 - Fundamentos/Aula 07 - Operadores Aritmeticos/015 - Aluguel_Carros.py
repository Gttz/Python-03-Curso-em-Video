km = float(input("Digite a quantidade de km percorridos:"))
dias = int(input("Digite a quantidade de dias que ele foi alugado: "))

PreçoTotal = (dias * 60) + (km * 0.15)

print("O preço total a pagar é de :{:.2f}".format(PreçoTotal))
