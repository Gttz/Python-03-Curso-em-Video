# 026: Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez.
# em que posição ela aparece a última vez.

frase = input("Digite qualquer coisa: ").strip().upper()

A = frase.count('A')
print(f"As vezes que apareceram a letra 'A' foram de: {A}")

print("A primeira letra A apareceu na posição: {}".format(frase.find('A')+1))

print("A última letra A apareceu na posição: {}".format(frase.rfind('A')+1))
