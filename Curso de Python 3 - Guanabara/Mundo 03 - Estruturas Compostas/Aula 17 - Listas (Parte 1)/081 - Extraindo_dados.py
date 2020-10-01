# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
cont = 0
print('Digite os números e digite valores negativos para sair.')
while True:
    n = int(input("Digite o número:"))
    lista.append(n)
    cont += 1
    if n < 0:
        print("Você escolheu sair...")
        lista.remove(-1)
        cont -= 1
        break
print(f"A quantidade de números digitados é de: {cont}")
lista.sort(reverse=True)
print(f"A lista de valores por ordem decrescente: {lista}")
if 5 in lista:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não foi encontrado na lista.")

