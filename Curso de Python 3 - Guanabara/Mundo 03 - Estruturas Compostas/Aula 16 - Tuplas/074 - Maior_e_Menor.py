# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
from time import sleep

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print("Gerando números aleatórios...")
sleep(1)
print(f"A listagem dos números gerados são: {tupla}")
print(f"O menor valor é {min(tupla)}\nO maior valor é {max(tupla)}")
