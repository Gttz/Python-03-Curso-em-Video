# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
# ------------------------------------------------------------------------------------------------
# JEITO QUE EU FIZ
sexo = 'teste'
while sexo != 'M' and sexo != 'F':
    sexo = str(input("Digite o sexo [M]/[F] :"))[0].upper().strip()
    if sexo != 'M' and sexo != 'F':
        print("Você digitou errado! Digite [M] para masculino e [F] para feminino!")
print("sexo {} registrado com sucesso!".format(sexo))
# ------------------------------------------------------------------------------------------------
# JEITO DO PROFESSOR
sexo = str(input("Digite o sexo [M][F] :"))
while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. Por favor, Informe seu sexo: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))
# ------------------------------------------------------------------------------------------------
