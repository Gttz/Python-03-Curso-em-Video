# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input("Digite o nome: "))

aluno['média'] = float(input("Digite a média de 0 a 10:"))
while aluno['média'] > 10:
    aluno['média'] = float(input("Digite a média de 0 a 10:"))

if 7 <= aluno['média'] <= 10:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f"{k} é igual a {v}")
