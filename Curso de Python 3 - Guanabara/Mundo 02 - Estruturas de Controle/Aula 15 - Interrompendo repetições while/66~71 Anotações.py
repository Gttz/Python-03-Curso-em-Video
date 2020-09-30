n = s = 0
# se usa 'while True' para uma repetição infinita caso não coloquemos o 'break' como na linha 06.
while True:
    n = int(input("Digite o número: "))
    if n == 999:
        break
    s += n
print(s)