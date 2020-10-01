# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def Maior(*numero):
    cont = maior = 0
    print('-=-' * 11)
    print(f'Analisando os Valores passados...')
    for valor in numero:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores.')
    print(f'O maior número foi {maior}')

Maior(5, 8, 9, 20, 12)

