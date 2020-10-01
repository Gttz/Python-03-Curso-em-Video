# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador(inicio, fim, passo):
    print('-=-' * 15)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 0

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    # caso o passo for negativo devemos transforma-lo em positivo

    if inicio < fim:
        for i in range(inicio, fim, passo):
            print(i, end=' ')
            sleep(0.3)
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            cont -= passo
            sleep(0.3)
        print('FIM')


#A)
contador(inicio=1, fim=11, passo=1)
#B)
contador(10, 0, 2)
#C)
print('-=-' * 15)
contador(int(input("Digite o ínicio: ")), int(input("Digite o fim:")), int(input("Digite o passo:")))


