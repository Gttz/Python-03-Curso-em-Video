# Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp = []
princ = []
print('-=-' * 10)
print("Bem vindo a listagem de pesos!")
print('-=-' * 10)
maior = menor = 0
while True:
    temp.append(str(input("Digite o nome: ")))
    temp.append(float(input("Digite o seu peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    continuar = str(input("Quer continuar? [S][N]")).capitalize()[0]
    while continuar not in 'SN':
        print('Você digitou errado! digite [S][N].')
        continuar = str(input("Quer continuar? [S][N]")).capitalize()[0]
    if continuar in 'N':
        print('Você escolheu parar...')
        break
print(f"Ao todo você cadastrou {len(princ)} pessoas.")

print(f'A listagem com as pessoas mais pesadas foi de : {maior}Kg que são: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print(f"\nA listagem das pessoas mais leves foi de : {menor}Kg que são: ", end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
