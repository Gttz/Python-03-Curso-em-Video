# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário  todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoas = dict()
total = list()
mulheres = list()
velhinhos = list()
soma = 0
while True:
    pessoas['nome'] = str(input("Digite o nome: "))
    pessoas['sexo'] = str(input('Digite o sexo M/F: ')).upper()[0]
    pessoas['idade'] = int(input("Digite a idade: "))
    soma += pessoas['idade']
    total.append(pessoas.copy())
    continuar = str(input("Deseja continuar? S/N")).capitalize()[0]
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar? S/N")).capitalize()[0]
    if continuar in 'N':
        break
print(f"A) Ao todo temos {len(total)} pessoas cadastradas.")
media = soma / len(total)
print(f'B) A média de todas as idades é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in total:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']}", end=' ')
print()
print('D) A lista com as pessoas acima da média é:', end='')
for p in total:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
print()
print('<< FINALMENTE ACABOU! >>')
