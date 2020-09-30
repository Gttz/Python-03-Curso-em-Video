# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

from termcolor import colored

print(colored("-=-", 'yellow') * 7)
print(colored("Conversor de bases", 'cyan'))
print(colored("-=-", 'yellow') * 7)

n = int(input("Digite um número inteiro:"))

base = int(input("Escolha uma das bases para conversão:\n"
                 "[1] converter para BINÁRIO\n"
                 "[2] converter para OCTAL\n"
                 "[3] converter para HEXADECIMAL\n"
                 "Sua opção: "))

if base == 1:
    print(colored("Conversor de bases para binário", 'cyan'))
    print("{} convertido para BINÁRIO é igual a {}".format(n, bin(n)[2:]))
elif base == 2:
    print(colored("Conversor de base para octal", 'magenta'))
    print("{} convertido para OCTAL é igual a: {}".format(n, oct(n)[2:]))
elif base == 3:
    print(colored("Conversor de base para hexadecimal", 'yellow'))
    print("{} convertido para HEXADECIMAL é igual a: {}".format(n, hex(n)[2:]))
else:
    print(colored("Digite um número válido!", 'red'))

# Obs: é [2:] para não pegar o ínicio do bin,oct,hex

