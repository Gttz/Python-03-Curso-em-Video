# Exercício Python 070: Crie um programa que leia o nome e o preco de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
from time import sleep

gasto_total = cont_caro = menor = cont = barato = 0
while True:
    nome = str(input("Digite o nome do produto: ")).capitalize()
    preco = float(input("Digite o preco do produto R$: "))
    cont += 1
    continuar = str(input("Você deseja continuar? [S][N]"))[0].capitalize()
    while continuar != 'S' and continuar != 'N':
        print("Você digitou errado! Digite novamente.")
        continuar = str(input("Você deseja continuar? [S][N]"))[0].capitalize()
    gasto_total += preco
    if preco > 1000:
        cont_caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if continuar == 'N':
        print("Você digitou 'N', Encerrando aplicação...")
        sleep(1)
        break
print(f"O gasto total da compra é: {gasto_total}")
print(f"A quantidade de produtos que custam mais de R$1000 são : {cont_caro}")
print(f"O produto mais barato custa R${menor} e o nome dele é: {barato}")

