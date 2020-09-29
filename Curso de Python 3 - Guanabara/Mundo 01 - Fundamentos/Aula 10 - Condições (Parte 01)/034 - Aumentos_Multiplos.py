# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário do funcionário: "))

if salario > 1250.00:
    aumento = salario + (salario * 10/100)
    print("O aumento do salário é de 10%, o novo salário dele ficou de:{:.2f}".format(aumento))
else:
    aumento = salario + (salario * 15/100)
    print("O aumento do salário é de 15%, o novo salário dele ficou de:{:.2f}".format(aumento))
