# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
from time import sleep

n = soma = subtracao = 0
multiplicacao = divisao = resto = 1
cont_valores = 0
while True:
    n = int(input("Digite o número (999 para parar) :"))
    cont_valores += 1
    if n == 999:
        print("Você digitou 999 parando aplicativo...")
        sleep(1)
        break
    soma += n
    subtracao -= n
    multiplicacao *= n
    divisao /= n
    resto %= n
print(f"A soma dos {cont_valores} números inteiros digitados foi de: {soma}")
print(f"A subtração dos {cont_valores} números inteiros digitados foi de: {subtracao}")
print(f"A multiplicação dos {cont_valores} números inteiros digitados foi de: {multiplicacao}")
print(f"A divisão dos {cont_valores} números inteiros digitados foi de: {divisao}")
print(f"O resto da divisão dos {cont_valores} números inteiros digitados foi de: {resto}")


