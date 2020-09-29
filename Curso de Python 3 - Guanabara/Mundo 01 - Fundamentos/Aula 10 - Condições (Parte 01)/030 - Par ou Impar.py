# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input("Digite o número:"))
par = n % 2

if par == 0:
    print("o número {} é par!".format(n))
else:
    print("O número {} é ímpar!".format(n))
