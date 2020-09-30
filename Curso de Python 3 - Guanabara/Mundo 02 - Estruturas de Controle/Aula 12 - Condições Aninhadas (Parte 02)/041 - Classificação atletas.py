# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from termcolor import colored
from datetime import date

print(colored("-=-", 'yellow') * 15)
print(colored("Bem vindo a Confederação Nacional de Natação!", 'cyan'))
print(colored("-=-", 'yellow') * 15)

print(colored("Este programa mostra em que categoria o atleta está de acordo com a sua idade!", 'cyan'))

ano = int(input("Digite o ano de nascimento do atleta: "))
atual = date.today().year
idade = atual - ano

print(colored("O atleta tem {} anos.".format(idade), 'cyan'))
if idade < 5:
    noano = date.today().year + 18 - idade
    print("Os jogos são apenas para crianças maiores de 9 anos, no ano de {} ela poderá se inscrever!".format(noano))
elif idade <= 9:
    print(colored("O atleta está na categoria MIRIM!", 'cyan'))
elif idade <= 14:
    print(colored("O atleta está na categoria INFANTIL", 'cyan'))
elif idade <= 19:
    print(colored("O atleta está na categoria JÚNIOR", 'cyan'))
elif idade <= 25:
    print(colored("O atleta está na categoria SÊNIOR", 'cyan'))
else:
    print(colored("O atleta está na categoria MASTER", 'cyan'))
