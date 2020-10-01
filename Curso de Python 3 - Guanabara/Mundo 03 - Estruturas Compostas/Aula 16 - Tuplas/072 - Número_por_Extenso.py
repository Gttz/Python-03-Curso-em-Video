# Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print("Bem vindo a contagem de números por extenso! Digite um número de 0 a 20"
      "\ncaso queira sair digite valores negativos")
while True:
    n = int(input("Digite um número de 0 a 20: "))
    while n > 20:
        print("Você digitou errado! Digite entre 0 e 20: ")
        n = int(input("Digite um número de 0 a 20: "))
    for pos, i in enumerate(tupla):
        if n == pos:
            print(f"Você digitou o número {tupla[pos]}")
    if n < 0:
        print("Encerrando aplicativo...")
        break
print('Obrigado volte sempre!')
