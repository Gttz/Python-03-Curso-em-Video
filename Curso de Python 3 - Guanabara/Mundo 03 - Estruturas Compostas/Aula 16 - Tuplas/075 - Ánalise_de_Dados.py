# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input("Digite o primeiro número:")),
         int(input("Digite o segundo número:")),
         int(input("Digite o terceiro número:")),
         int(input("Digite o quarto número:")))
print(f"Você digitou os valores: {tupla}")
print(f'A quantidade de vezes do número 9 digitado é: {tupla.count(9)}')
if 3 in tupla:
    print(f'O número 3 foi digitado na {tupla.index(3)}º posição ')
else:
    print("O número 3 não foi localizado na tupla.")
print("Os valores pares digitados foram:", end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

