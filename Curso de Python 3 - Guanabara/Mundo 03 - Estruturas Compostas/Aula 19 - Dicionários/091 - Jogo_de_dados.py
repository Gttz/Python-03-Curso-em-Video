# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

dado = dict()
ranking = dict()
# randomiza os dados
for i in range(1, 5):
    dado[f'Jogador {i}'] = randint(1, 6)

# imprime oque cada um tirou
for k, v in dado.items():
    print(f'O {k} tirou {v}')
    sleep(1)

# ordena e imprime o ranking
#Usamos o comando sort + o comando 'itemgetter' e usamos o reverse pois estava ordenado ao contrário
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
