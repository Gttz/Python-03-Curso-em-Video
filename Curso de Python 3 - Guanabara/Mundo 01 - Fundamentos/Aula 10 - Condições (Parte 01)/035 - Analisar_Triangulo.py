# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.
from termcolor import colored
print(colored('-=-', 'yellow') * 9)
print(colored('Analisando Triângulos...', 'blue'))
print(colored('-=-', 'yellow') * 9)

r1 = int(input("Primeiro segmento:"))
r2 = int(input("Segundo segmento:"))
r3 = int(input("Terceiro segmento:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(colored("Os segmentos acima podem formar triângulos.", 'green'))
else:
    print(colored("Os segmentos acima não podem formar triângulos.", 'red'))
