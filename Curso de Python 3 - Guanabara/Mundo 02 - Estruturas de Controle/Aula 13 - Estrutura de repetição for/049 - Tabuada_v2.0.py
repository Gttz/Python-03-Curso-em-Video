n = int(input("Digite o número que quer ver na tabuada: "))

for i in range(0, 11):
    print("{} x {:2} = {}".format(n, i, n*i))
