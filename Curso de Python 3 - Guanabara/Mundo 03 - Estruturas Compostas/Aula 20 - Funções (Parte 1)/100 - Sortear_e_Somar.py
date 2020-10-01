# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia(listinha):
    print('Sorteando 5 valores da lista.', end='')
    for i in range(0, 5):
        lista.append(randint(0, 60))
    print(lista)


def somaPar(listinha):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {listinha} temos o resultado {soma}')


lista = list()
sorteia(lista)
somaPar(lista)

