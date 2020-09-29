# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distância = float(input("Digite a distância da viagem:"))
if distância <= 200:
    passagem = distância * 0.50
    print("A sua viagem é normal, portanto a passagem ficou: {:.2f}".format(passagem))
else:
    passagem = distância * 0.45
    print("A sua viagem é longa, portanto a passagem ficou: {:.2f}".format(passagem))

# forma em apenas uma linha
# passagem = distância * 0.50 if distância <=200 else distância * 0.45
# print("E o preço da passagem será de R$: {:.2f}".format(passagem))
