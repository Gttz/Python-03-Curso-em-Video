#Com módulos
from math import hypot
oposto = float(input("Digite o cateto oposto:"))
adjacente = float(input("Digite o cateto adjacente:"))
Hiper = hypot(oposto, adjacente)
print("A hipertenusa vai medir: {:.2f}".format(Hiper))

# Sem módulos
oposto = float(input("Digite o cateto oposto:"))
adjacente = float(input("Digite o cateto adjacente:"))

Hiper = (oposto**2+adjacente**2) ** (1/2)

print("A hipertenusa vai medir: {:.2f}".format(Hiper))
