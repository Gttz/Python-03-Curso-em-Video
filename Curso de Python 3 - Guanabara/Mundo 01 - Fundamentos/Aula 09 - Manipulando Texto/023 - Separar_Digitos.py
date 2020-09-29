# 023:Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# 023:Make a program that reads a number from 0 to 9999 and shows each of the separate digits on the screen.

num = int(input("Digite o número:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o número: {}".format(num))

print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")