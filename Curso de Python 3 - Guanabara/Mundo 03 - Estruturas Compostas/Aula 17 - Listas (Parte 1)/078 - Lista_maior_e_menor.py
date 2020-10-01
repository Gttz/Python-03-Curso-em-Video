# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()

for i in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {i}: ")))
print('-=-' * 15)
print(f'Você digitou os valores: {lista}')
print(f"O maior valor da lista foi {max(lista)} na posição ", end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print()
print(f"O menor valor da lista foi {min(lista)} na posição ", end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')

