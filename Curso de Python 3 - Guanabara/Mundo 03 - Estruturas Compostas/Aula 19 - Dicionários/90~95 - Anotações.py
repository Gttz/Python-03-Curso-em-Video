# dados = dict()
# dados['nome'] = 'lucas'
# dados['idade'] = 21
# dados['sexo'] = 'M'

#todo print(dados['nome'])
# #Pega apenas os valores
# print(dados.values())
# # Pega as chaves ex : 'nome' 'idade' 'sexo'
# print(dados.keys())
# # Pega tudo do dict
# print(dados.items())
# # Um for onde 'K' são as chaves e 'V' são os valores
# for k, v in dados.items():
#     print(f'O {k} é {v}')

# pessoas = {'nome': 'Lucas', 'idade': '21', 'sexo': 'M'}
# # adiciona uma chave e um elemento, se formatar ele vai lá pra cima
# pessoas['Peso'] = 98.5
# # apaga uma chave e um elemento
# del pessoas['sexo']
#
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#
#todo # acessa todos as chaves da lista
# for k in pessoas.keys():
#     print(k)
# print()
# # acessa todos os elementos da lista
# for v in pessoas.values():
#     print(v)
# # mostra todos organizados
# for k, v in pessoas.items():
#     print(f"{k} = {v}")

# brasil = list()
# # coloca as chaves e os elementos manualmente
# estado1 = {'UF': 'Rio de janeiro', 'sigla': 'RJ'}
# estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0])
estado = dict()
brasil = list()
for i in range(0, 3):
    estado['UF'] = str(input("Unidade federativa: "))
    estado['Sigla'] = str(input("Sigla do estado: "))
    # se dermos o comando 'append' da lista dá erro e copia elementos repetidos
    #brasil.append(estado)
    # usamos o comando 'copy' que pertence ao dict
    brasil.append(estado.copy())

# acessa as chaves e os valores.
for e in brasil:
    for k, v in e.items():
        print(f' {k} = {v}')
