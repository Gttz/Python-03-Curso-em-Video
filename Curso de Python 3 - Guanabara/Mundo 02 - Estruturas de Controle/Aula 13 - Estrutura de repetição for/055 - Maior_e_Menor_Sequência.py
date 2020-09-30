# Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# peso = int(input(f'Digite o peso da 1º pessoa: '))

for i in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa:".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print("O maior peso foi de {}Kg e o menor peso foi de {}Kg".format(maior, menor))

