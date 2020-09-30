# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento, seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input("Digite o ano que você nasceu:"))
atual = date.today().year
idade = atual - ano

if idade < 18:
    Ano = atual + 18 - idade
    print("Você ainda vai se alistar ao serviço militar, faltam {} anos.".format(18 - idade))
    print("Seu alistamento será em {}.".format(Ano))
elif idade == 18:
    print("Esta é a hora exata para se alistar!")
else:
    Ano = atual + 18 - idade
    print("Já passou da hora do alistamento, passou-se {} anos.".format(idade - 18))
    print("Seu alistamento foi em {}.".format(Ano))
