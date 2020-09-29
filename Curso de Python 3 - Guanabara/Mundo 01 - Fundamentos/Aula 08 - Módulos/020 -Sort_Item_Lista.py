from random import shuffle

lista = []

aluno1 = str(input("Aluno 1: "))
lista.append(aluno1)
aluno2 = str(input("Aluno 2: "))
lista.append(aluno2)
aluno3 = str(input("Aluno 3: "))
lista.append(aluno3)
aluno4 = str(input("Aluno 4: "))
lista.append(aluno4)

shuffle(lista)

print("A ordem de apresentação será: {} ".format(lista))
