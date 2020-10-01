# Python 092:Crie um programa que leia nome,ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um
# dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = dict()

dados['nome'] = str(input("Digite o nome: ")).capitalize()
ano = int(input("Digite o ano de nascimento: "))
dados['Idade'] = date.today().year - ano
dados['CTPS'] = int(input("Digite o número (0 não tem): "))


if dados['CTPS'] != 0:
    dados['AnoContratado'] = int(input("Digite o ano de contratação:"))
    dados['Salario'] = float(input("Digite o salário R$: "))
    dados['Aposentadoria'] = dados['Idade'] + (dados['AnoContratado'] + 35) - date.today().year

for k, v in dados.items():
    print(f'{k} tem o valor {v}')
