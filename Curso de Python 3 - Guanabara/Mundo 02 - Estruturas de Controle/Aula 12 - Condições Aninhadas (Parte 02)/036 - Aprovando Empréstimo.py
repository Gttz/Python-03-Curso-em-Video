# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.
from termcolor import colored

print(colored('-=-', 'yellow') * 9)
print(colored('Program My Python, My Life', 'green'))
print(colored('-=-', 'yellow') * 9)

casa = float(input(colored("Valor da casa: R$", 'green')))
salario = float(input(colored("Salário do comprador: R$", 'green')))
anos = int(input(colored("Quantos anos de financiamento: ", 'green')))

prestacao = casa / (anos * 12)
minimo = salario * 30/100

print("Para pagar uma casa de R${:.2f} em {} anos ".format(casa, anos), end='')
print("A prestação será de R${:.2f}".format(prestacao))
if prestacao <= minimo:
    print(colored("Empréstimo pode ser CONCEDIDO!", 'green'))
else:
    print(colored("Empréstimo NEGADO!", 'red'))
