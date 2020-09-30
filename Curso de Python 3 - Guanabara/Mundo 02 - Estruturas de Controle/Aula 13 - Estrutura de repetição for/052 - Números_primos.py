# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite o numero:"))
tot = 0

for i in range(1, n + 1):
    if n % i == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print("{} ".format(i), end=' ')
print('\n\033[m0 O número {} foi divisível {} vezes'.format(n, tot))

if tot == 2:
    print("É por isso que ele é primo!")
else:
    print("É por isso que ele não é primo!")
