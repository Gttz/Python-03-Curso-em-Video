# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# # composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
# cada aluno individualmente.
# Um menu com 4 escolhas: sair/ adicionar aluno / remover aluno/ ver notas
# a lista sempre deverá ficar em ordem alfabetica

ficha = list()
while True:
    nome = str(input("Digite o nome: "))
    nota1 = float(input("Digite a nota 1:"))
    nota2 = float(input("Digite a nota 2:"))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Deseja continuar? [S][N]")).strip().capitalize()[0]
    while resp not in 'SN':
        resp = str(input("Deseja continuar? [S][N]")).strip().capitalize()[0]
    if resp in 'N':
        break

print('-=-' * 10)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opc = int(input("Quer ver as notas de qual aluno? 999 para parar."))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print("<<< VOLTE SEMPRE! >>>")


