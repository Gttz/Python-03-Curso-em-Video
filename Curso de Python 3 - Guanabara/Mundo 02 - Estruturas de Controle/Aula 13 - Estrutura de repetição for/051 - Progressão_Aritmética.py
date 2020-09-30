# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

t = int(input("Digite o primeiro termo da PA:"))
r = int(input("Digite a razão da PA:"))
num = 0
for i in range(t, 10, r):
    num += r
    print(num)
