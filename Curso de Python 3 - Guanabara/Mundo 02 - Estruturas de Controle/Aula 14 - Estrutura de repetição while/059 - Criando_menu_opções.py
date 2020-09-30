# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
e = 0
while e != 5:
    print("-=-" * 10)
    print(""
          "[1] SOMAR +\n"
          "[2] MULTIPLICAR *\n"
          "[3] MAIOR >\n"
          "[4] NOVOS NÚMEROS \n"
          "[5] SAIR DO PROGRAMA")
    e = int(input("Sua escolha: "))
    print("-=-" * 10)
    if e == 1:
        print("{} + {} = {}".format(n1, n2, n1 + n2))
    elif e == 2:
        print("{} x {} = {}".format(n1, n2, n1 * n2))
    elif e == 3:
        print("{} > {} = {}".format(n1, n2, n1 > n2))
    elif e == 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    elif e == 5:
        print("Você escolhe sair do programa!")
    else:
        print("Você digitou o comando errado, escolha entre [1][2][3][4] !")
print("Obrigado, volte sempre!")
print("-=-" * 10)


