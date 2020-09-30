# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
from time import sleep

print("Olá, bem vindo a tabuada v3.0! Digite o número que quer ver da tabuada\n"
      "caso queira parar digite um valor negativo! Ex : -1")
n = 0
while True:
    n = int(input("Quer ver a tabuada de que valor?"))
    if n < 0:
        print(f"Você digitou {n}. Parando programa...")
        sleep(1)
        break
    for i in range(0, 11):
        m = n * i
        print(f"{n} x {i} = {m}")
print("Obrigado e volte sempre!")

