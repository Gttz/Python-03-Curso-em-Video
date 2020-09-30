#r = 'S'
#while r == 'S':
#    n = int(input("Digite o número: "))
#    r = str(input("Quer continuar? [S/N]")).upper() o problema é q ta aceitando outras letras para parada!
#print("FIM")

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite o número:"))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} pares e {} ímpares.".format(par, impar))
