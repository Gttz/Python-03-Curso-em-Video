# Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,desconsiderando os espaços.
# Ex : APOS A SOPA
# Ex : A SACADA DA CASA
# EX : A TORRE DA DERROTA

frase = str(input("Digite a frase:")).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#inverso = junto[::-1] FORMA QUE SUBSTITUIRIA O FOR
for letra in range(len(junto) - 1, -1, -1):
    # -1:o primeiro -1 é para acessar a última posição,
    # -1:a primeira letra é 0, mas lembrar que ele vai de trás pra frente
    # -1: ele vai andar pra trás!
    inverso += junto[letra]

print(inverso)
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("Não é um palíndromo!")
