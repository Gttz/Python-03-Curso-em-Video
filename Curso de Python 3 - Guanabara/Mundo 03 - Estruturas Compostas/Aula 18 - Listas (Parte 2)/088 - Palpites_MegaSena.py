# Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = list()
print('-=-' * 5)
print('MEGA SENA!')
print('-=-' * 5)
jogos = int(input('Digite a quantidade de jogos a serem gerados: '))
print(f'\n----------SORTEANDO {jogos} JOGOS----------')
for k in range(0, jogos):
    lista.clear()
    cont = 0
    while True:
        if cont == 6:
            break
        numeros = randint(1, 60)
        if numeros not in lista:
            cont += 1
            lista.append(numeros)
    sleep(0.5)
    lista.sort()
    print(f'Jogo {k + 1} : {lista}')
print('-=-' * 5, '< BOA SORTE! >', '-=-' * 5)

