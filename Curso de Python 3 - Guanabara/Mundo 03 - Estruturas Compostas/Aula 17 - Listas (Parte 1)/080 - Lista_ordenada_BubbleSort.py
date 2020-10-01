# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
# lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()

for i in range(1, 6):
    lista.append(int(input(f"Digite o valor para a {i}º posição:")))

for i in range(0, len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            temp = lista[j]
            lista[j] = lista[i]
            lista[i] = temp

print(f"A lista ordenada é: {lista}")
