# Exercício Python 040: Crie um programa que leia duas notas de um aluno e
# calcule sua média mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
from termcolor import colored

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media < 5:
    print(colored("Sua média foi de {} portanto está REPROVADO.".format(media), 'red'))
elif 5 <= media < 7:
    print(colored("Sua média foi de {} portanto está de RECUPERAÇÃO.".format(media), 'magenta'))
elif 7 <= media <= 10:
    print(colored("Sua média foi de {} portanto está APROVADO.".format(media), 'green'))
else:
    print(colored("A média deve ser 0 a 10, Digite valores menores do que 10 nas notas!", 'blue'))
