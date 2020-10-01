# abre a ajuda do python
# help()
# mostra a ajuda pedindo diretamente
# print(input.__doc__)


def contador(inicio, fim, passo):
    """Também podemos colocar 'passo=0' para termos um 'parâmetro opcional'
    -> Faz uma contagem na tela
    :param inicio: início da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    OBS : também podemos criar um HELP da nossa própria função usando três '''.
    """
    if inicio < fim:
        for i in range(inicio, fim, passo):
            print(i, end=' ')
        print('FIM')
# contador(1, 150, 5)
# help(contador)


def soma(a, b, c=0):
    """
    Também podemos colocar o valor como 'c=0' para termos um 'parâmetro opcional'
    """
    s = a + b + c
    print(s)
# soma(5, 5)


def funcao():
    #já a variável N1 de dentro da função é LOCAL
    n1 = 4
    print(f'N1 dentro vale {n1}')
# a variável n1 é GLOBAL
# n1 = 8
# funcao()
# print(f'N1 fora vale {n1}')


def soma2(a=0, b=0, c=0):
    s = a + b + c
    # FINALMENTE VIMOS O RETURN NO PYTHON! MESMA COISA DO JAVA!
    return s
# r1 = soma2(5, 10, 19)
# r2 = soma2(15, 20, 29)
# r3 = soma2(35, 50, 99)
# print(f"Os meus cálculos deram {r1},{r2} e{r3}")


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    # exemplo da função 'return' com fatorial
    return f
# n = fatorial(10)
# print(n)


def par(num):
    # também podemos retornar valores booleanos
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input("Digite o número:"))
# podemos jogar em um if a função def
if par(n):
    print("É par!")
else:
    print("É ímpar!")
