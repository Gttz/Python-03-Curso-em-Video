# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao
# final, mostre o conteúdo das três listas geradas.
lista = list()
pares = list()
impares = list()

while True:
    n = int(input("Digite os números:"))
    lista.append(n)
    r = str(input("Quer continuar? [S][N]")).capitalize()[0]
    while r not in 'SN':
        print("Você digitou errado! Digite [S][N]")
        r = str(input("Quer continuar? [S][N]")).capitalize()[0]
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if r in 'N':
        print("Saindo do programa...")
        break
print(f'A lista padrão recebeu os valores: {lista}')
print(f"A lista de pares recebeu os valores: {pares}")
print(f'A lista de ímpares recebeu os valores: {impares}')
