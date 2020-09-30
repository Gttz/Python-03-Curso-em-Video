# Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao  usuário qual
# será o valor a ser sacado (número inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues.
# OBS: considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.

saque = float(input("Digite o valor a ser retirado R$:"))

total = saque
ced = 50
totced = 0
while True:
    if totced >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R$: {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

# Algo errado nesse , não consegui fazer solo t.t
