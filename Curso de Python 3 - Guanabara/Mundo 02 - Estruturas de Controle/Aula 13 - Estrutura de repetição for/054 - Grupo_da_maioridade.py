# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(i)))
    idade = date.today().year - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print("Ao todo tivemos {} pessoas maiores de idade.".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))
