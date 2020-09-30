# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
lista = []
cont = 0
n = int(input("Digite o número: "))
lista.append(n)
r = str(input("Você quer continuar? [S][N]")).upper()
maior = n
menor = n
while r == 'S':
    n = int(input("Digite o número: "))
    cont += 1
    lista.append(n)
    r = str(input("Você quer continuar? [S][N]")).upper()
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
media = sum(lista) / len(lista)
print("A média de todos os números inteiros é de: {}".format(media))
print("O maior valor é: {}\nO menor valor é: {}".format(maior, menor))
