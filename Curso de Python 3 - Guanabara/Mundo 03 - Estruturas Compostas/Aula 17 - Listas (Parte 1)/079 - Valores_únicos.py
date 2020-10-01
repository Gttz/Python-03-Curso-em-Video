# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
lista = list()

while True:
    n = int(input("Digite o valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não irei adicionar.")

    continuar = str(input("Continuar? [S/N]")).upper()[0]
    while continuar != 'S' and continuar != 'N':
        print("Você digitou errado!")
        continuar = str(input("Continuar? [S/N]")).upper()[0]
    if continuar == 'N':
        print("Você escolheu PARAR...")
        break
print("-=-" * 15)
print(f"Você digitou os valores: {lista}")
print("-=-" * 15)

# Fiz com ajuda! , Não me aguentei e fui olhar, só não soube fazer o 'if n not in lista'
