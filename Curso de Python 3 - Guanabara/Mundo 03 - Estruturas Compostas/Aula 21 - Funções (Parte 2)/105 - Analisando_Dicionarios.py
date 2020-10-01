# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)


def notas(*nota, sit=False):
    dic = dict()
    dic['total'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    media = sum(nota) / len(nota)
    dic['média'] = media
    if sit:
        if media >= 7:
            dic['Situação'] = 'Ótima'
        elif media >= 5:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Ruim'
        return dic


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
