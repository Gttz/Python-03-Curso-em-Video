#Com módulos
from math import trunc
n = float(input("Digite um numero:"))
print("O número {} tem a parte inteira de {}".format(n, trunc(n)))

#Sem módulos
n = float(input("Digite um número:"))
print("O número {} tem a parte inteira de {}".format(n, int(n)))
