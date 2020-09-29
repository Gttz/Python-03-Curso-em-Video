# 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip().lower().split()
print('Seu nome contém Silva?', 'silva' in nome)

# Observação: Pode se ter um nome 'SILVANA' e cair como 'SILVA'
