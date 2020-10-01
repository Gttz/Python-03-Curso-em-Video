# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.


def voto(ano):
    # é melhor importamos dentro da função para economizar mémoria.
    from datetime import date

    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: voto NEGADO'
    elif idade >= 15 and idade < 18 or idade >= 65:
        return f'Com {idade} anos: voto OPCIONAL'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: voto OBRIGATORIO'


saida = voto(int(input("Digite o ano que nasceu: ")))
print(saida)


