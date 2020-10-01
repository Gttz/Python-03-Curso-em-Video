# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.


def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {terreno}km².')


area(float(input('Digite a largura:')), float(input('Digite o comprimento: ')))

