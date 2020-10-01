def mensagem(msg):
    print('-=-' * 30)
    print(f'{msg}')
    print('-=-' * 30)


def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')


def somamelhorada(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} que tem o tamanho de {tam}')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa principal
mensagem('Testando...')
# soma os valores
soma(5, 5)
# também podemos fazer ao contrário
soma(b=9, a=5)
# uma soma melhorada onde soma todos os valores passados
somamelhorada(5, 5, 8, 4, 2)
# conta todos os números coloca em uma tupla e ve o tamanho.
contador(7, 8, 9, 6, 2)

# cria uma lista e dobra o valor dela
lista = [7, 15, 5, 9, 4]
print(lista)
dobra(lista)
print(lista)
