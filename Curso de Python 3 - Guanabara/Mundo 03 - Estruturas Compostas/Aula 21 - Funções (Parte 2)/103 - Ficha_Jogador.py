# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome, gols):
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols na partida')


ficha(input("Nome do jogador:").strip(), input("Total de gols:").strip())


