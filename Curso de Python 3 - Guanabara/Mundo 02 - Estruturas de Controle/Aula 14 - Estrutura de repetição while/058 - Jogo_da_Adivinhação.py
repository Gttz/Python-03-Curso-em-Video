# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
from termcolor import colored

print(colored('-=-', 'yellow') * 13)
print(colored("Estou pensando em um número de 0 a 10...", 'blue'))
print(colored('-=-', 'yellow') * 13)
sleep(1.5)
pensado = randint(0, 10)
print(colored("Já pensei! sua vez de tentar descobrir!", 'blue'))
print(colored('-=-', 'yellow') * 13)
adivinha = -1
cont = 0
while adivinha != pensado:
    adivinha = int(input("Chute o número que o computador pensou: "))
    if pensado != adivinha:
        cont += 1
        if adivinha < pensado:
            print(colored("Dica do Além: +!", 'magenta'))
        elif adivinha > pensado:
            print(colored("Dica do Além: -!", 'magenta'))

if cont == 0:
    print(colored('You WIN!', 'magenta'))
    print(colored("Você acertou em apenas 1º TENTATIVA? Impossível, tá de HACK.", 'magenta'))
elif cont <= 5:
    print(colored('You WIN!', 'green'))
    print(colored("Parábens,você acertou em {}º tentativas,Você errou algumas,mas ainda conseguiu me vencer!", 'green')
          .format(cont))
elif cont <= 9:
    print(colored('You WIN!', 'cyan'))
    print(colored("Você não foi tão mal assim, você acertou em {}º tentativas,você foi razoável!", 'cyan').format(cont))
elif cont >= 10:
    print(colored('You WIN!', 'red'))
    print(colored("Você acertou em {}º tentativas,RESPEITE A M-A-C-H-I-N-E M-A-S-T-E-R MUHAHAHAH!", 'red').format(cont))
