# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint
from time import sleep
from termcolor import colored

print(colored('-=-', 'yellow') * 13)
print(colored("Estou pensando em um número de 0 a 5...", 'blue'))
print(colored('-=-', 'yellow') * 13)
sleep(2)
pensado = randint(0, 5)
print(colored("Já pensei! sua vez de tentar descobrir!", 'blue'))
print(colored('-=-', 'yellow') * 13)

adivinha = int(input("Chute o número que o computador pensou: "))
print("O número que pensei foooi : {}".format(pensado))
if pensado == adivinha:
    print(colored('Você lê mentes por acaso? You win!', 'green'))
else:
    print(colored("Sou a máquina mais esperta do universo ! You lose!", 'red'))
