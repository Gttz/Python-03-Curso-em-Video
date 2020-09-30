# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from termcolor import colored

idades = []
contdemuie = 0
idadedovei = 0

print(colored("-=-", 'red') * 10)
print(colored("O EXERCICIO DIFICIN DO CARAY!", 'yellow'))
print(colored("-=-", 'red') * 10)

for i in range(1, 5):
    print(colored("\n------- {}ª PESSOA -------", 'yellow').format(i))
    nome = str(input("Digite o nome: ")).capitalize().strip()
    idade = int(input("Digite a idade: "))
    idades.append(idade)
    sexo = str(input("Digite o sexo [M]/[F]: "))[0].capitalize().strip()

    if i == 1 and sexo == 'M':
        idadedovei = idade
        nomedovei = nome
    if sexo == 'M' and idade > idadedovei:
        idadedovei = idade
        nomedovei = nome
    if sexo == 'F':
        if idade <= 20:
            contdemuie += 1

media = (idades[0] + idades[1] + idades[2] + idades[3]) / 4

print("A media da idade do grupo é: {}".format(media))

print("A maior idade foi de: {}".format(max(idades)))
print("e o nome do homem mais velho é: {}".format(nomedovei))

print("A quantidade de mulheres com menos de 20 anos é: {}".format(contdemuie))
