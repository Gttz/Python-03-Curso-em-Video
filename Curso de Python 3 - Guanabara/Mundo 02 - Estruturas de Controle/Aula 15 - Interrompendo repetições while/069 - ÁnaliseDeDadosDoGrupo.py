# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
from time import sleep

cont_idade = 0
cont_homem = 0
cont_mulher = 0
while True:
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo: [M][F]: ")[0].capitalize()
    while sexo != 'M' and sexo != 'F':
        print("Digite um valor válido! [M][F]")
        sexo = input("Digite o seu sexo: [M][F]: ")[0].capitalize()
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homem += 1
    if idade < 20 and sexo == 'F':
        cont_mulher += 1
    continuar = input("Deseja continuar? [S][N]")[0].capitalize()
    while continuar != 'S' and continuar != 'N':
        print("Digite um valor válido! [S][N]")
        continuar = input("Deseja continuar? [S][N]")[0].capitalize()
    if continuar == 'N':
        print("Você decidiu parar a aplicação...")
        sleep(1)
        break

print(f"A quantidade de pessoas maiores de 18 anos é de: {cont_idade}")
print(f"A quantidade de homens que foram cadastrados é de: {cont_homem}")
print(f"A quantidade de mulheres menores de 20 anos é de: {cont_mulher}")

