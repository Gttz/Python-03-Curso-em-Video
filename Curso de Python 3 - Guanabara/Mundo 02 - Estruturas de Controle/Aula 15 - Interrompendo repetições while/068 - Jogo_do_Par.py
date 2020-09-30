# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
from time import sleep
from random import randint
from termcolor import colored

vitorias = 0
derrota = False
while True:
    jogada = str(input("Digite a sua jogada, [PAR] ou [IMPAR]: ")).upper().strip()
    while jogada != 'PAR' and jogada != 'IMPAR':
        print("Você digitou a jogada errada! Digite [PAR] ou [IMPAR]")
        jogada = str(input("Digite a sua jogada, [PAR] ou [IMPAR]: ")).upper()
    jogador = int(input("Digite o número que quer jogar: "))
    print(colored("-=-", 'red') * 15)
    print(colored("Máquina: Minha vez de escolher o número...", 'cyan'))
    print(colored("-=-", 'red') * 15)
    sleep(1)
    computador = randint(0, 10)
    parouimpar = jogador + computador
    print(colored(f"Você escolheu {jogador} e a máquina escolheu {computador} a soma entre eles é de : {parouimpar}",
                  'yellow'))
    par = parouimpar % 2
    if par == 0:
        print(colored(f"O número {parouimpar} é PAR!", 'magenta'))
        if jogada == 'PAR':
            print(colored("Você ganhou a rodada! Iniciando outra...", 'green'))
            vitorias += 1
        else:
            print(colored("Você perdeu a rodada! O jogo será encerrado.", 'red'))
            derrota = True
    elif par > 0:
        print(colored(f"O número {parouimpar} é IMPAR!", 'magenta'))
        if jogada == 'IMPAR':
            print(colored("Você ganhou a rodada! Iniciando outra...", 'green'))
            vitorias += 1
        else:
            print(colored("Você perdeu a rodada! O jogo será encerrado...", 'red'))
            derrota = True
    if derrota:
        sleep(1)
        print(colored(f'A quantidade de vitórias consecutivas foi de {vitorias}', 'green'))
        print(colored("Fim de jogo, encerrando programa...", 'magenta'))
        sleep(0.5)
        break
print(colored("Obrigado e volte sempre!", 'magenta'))


