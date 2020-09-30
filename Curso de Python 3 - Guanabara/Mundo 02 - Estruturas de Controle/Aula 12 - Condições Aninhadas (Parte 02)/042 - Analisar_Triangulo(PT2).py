#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ESCALENO: todos os lados diferentes
#- ISÓSCELES: dois lados iguais, um diferente
from termcolor import colored
print(colored('-=-', 'yellow') * 9)
print(colored('Analisando Triângulos...', 'blue'))
print(colored('-=-', 'yellow') * 9)

r1 = int(input("Primeiro segmento:"))
r2 = int(input("Segundo segmento:"))
r3 = int(input("Terceiro segmento:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(colored("Os segmentos acima podem formar o triângulo: ", 'green'), end='')
    if r1 == r2 == r3:
        print(colored("EQUILÁTERO!", 'cyan'))
    elif r1 != r2 != r3 != r1:
        print(colored("ESCALENO!", 'blue'))
    else:
        print(colored("ISÓSCELES!", 'yellow'))
else:
    print(colored("Os segmentos acima não podem formar triângulos.", 'red'))
