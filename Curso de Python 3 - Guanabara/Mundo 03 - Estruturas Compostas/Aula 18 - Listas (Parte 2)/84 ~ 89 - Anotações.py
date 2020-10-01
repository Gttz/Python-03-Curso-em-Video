# padrao = list()
# Coloca gustavo e 25 na lista padrao
# padrao.append('Gustavo')
# padrao.append(25)
#
# #cria uma lista copia
# copia = list()
# # tudo que está na lista padrão foi copiado para a lista copia
# copia.append(padrao[:])
# # jeito errado de fazer:
# # copia.append(padrao)
#
# #insere elementos na padrão
# padrao[0] = 'Maria'
# padrao[1] = 25
# # insere novamente tudo da padrão para a copia
# copia.append(padrao[:])
# # jeito errado de fazer:
# #copia.append(padrao)
# print(padrao)
# print(copia)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#
# mostra 'joão e 19'
# print(galera[0])
# # mostra 'joaquim'
# print(galera[2][0])
# # mostra '45'
# print(galera[3][1])
#
#  for p in galera:
#     # pega tudo
#     print(p)
#     # pega apenas os nomes
#     print(p[0])
#     # pega apenas as idades
#     print(p[1])
#     # jeito bonito
#     print(f'{p[0]} tem {p[1]} de idade.')

povo = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite a idade: ")))
    #lembrar sempre do '[:]'
    povo.append(dado[:])
    dado.clear()
print(povo)
totmaior = totmenor = 0
for p in povo:
    if p[1] > 18:
        print(f"{p[0]} é maior de idade!")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade!")
        totmenor += 1
print(f"Temos {totmaior} maiores e {totmenor} menores de idade.")