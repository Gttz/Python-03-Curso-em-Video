# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado! A multa vai custar: {:.2f}".format(multa))
