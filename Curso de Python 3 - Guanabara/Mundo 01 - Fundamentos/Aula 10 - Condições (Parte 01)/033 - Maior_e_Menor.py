# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

menor = n1
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3
print("O número menor é o {}".format(menor))

maior = n1
if n2 > maior:
    n2 = maior
if n3 > maior:
    n3 = maior
print("O número maior é o {}".format(maior))

# Jeito simples
# lista = [n1, n2, n3]
# print(f"O número menor é o {min(lista)}")
# print(f"O número maior é o {max(lista)}")
