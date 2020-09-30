# Exercício Python 044: Elabore um programa que calcule o valor a ser pago
# por um produto considerando o seu preço normal e condicao de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
from termcolor import colored

print(colored("-=-", 'yellow') * 8)
print(colored("LOJINHA DO SEU JOAQUIM", 'cyan'))
print(colored("-=-", 'yellow') * 8)

produto = float(input("Digite o valor do produto: R$"))
while True:
    condicao = int(input("Escolha entre:\n"
                         "[1] a vista dinheiro/cheque (10% de desconto).\n"
                         "[2] a vista no cartão (5% de desconto).\n"
                         "[3] em até 2x no cartão (preço formal).\n"
                         "[4] 3x ou mais no cartão (20% de juros).\n"
                         "[5] Sair"))

    print(colored("Sua escolha foi: {}".format(condicao), 'magenta'))

    while condicao > 5:
        print(colored("Você deve digitar uma opção valida!", 'red'))
        condicao = int(input("Escolha entre:\n"
                             "[1] a vista dinheiro/cheque (10% de desconto).\n"
                             "[2] a vista no cartão (5% de desconto).\n"
                             "[3] em até 2x no cartão (preço formal).\n"
                             "[4] 3x ou mais no cartão (20% de juros).\n"
                             "[5] Sair"))
    if condicao == 1:
        produtoAtt = produto - (produto * 10 / 100)
        print(colored("O seu pagamento vai ser á vista no dinheiro/cheque e ganhará 10% de desconto", 'green'))
        print("Portanto o produto que era de {}, com o desconto de 10% ficou: {}".format(produto, produtoAtt))
    elif condicao == 2:
        produtoAtt = produto - (produto * 5 / 100)
        print(colored("O seu pagamento vai ser á vista no cartão e ganhará 5% de desconto", 'green'))
        print("Portanto o produto que era de {}, com o desconto de 5% ficou: {}".format(produto, produtoAtt))
    elif condicao == 3:
        print(colored("O seu pagamento vai ser em até 2x no cartão e pagará o preço formal", 'yellow'))
        print("Portanto o produto com o preço formal ficou: {} ".format(produto))
    elif condicao == 4:
        produtoAtt = produto + (produto * 20 / 100)
        print(colored("O seu pagamento vai ser em até 3x ou mais no cartão e terá 20% de juros", 'red'))
        parcela = int(input('Quantas parcelas?'))
        print('Sua compra parcelada em {}x vai ser R${:.2f} com JUROS de R${}'
              .format(parcela, (produtoAtt / parcela), (produtoAtt - produto)))
    elif condicao == 5:
        print(colored("Você escolheu por parar, volte sempre!", 'magenta'))
        break

