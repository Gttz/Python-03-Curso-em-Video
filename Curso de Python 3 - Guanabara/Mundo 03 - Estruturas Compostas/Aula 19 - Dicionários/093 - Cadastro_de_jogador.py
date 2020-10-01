# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
lista = list()
dados['Nome'] = str(input("Nome do jogador:")).strip().capitalize()
partidas = int(input("Partidas jogadas:"))
for i in range(0, partidas):
    lista.append(int(input(f"Número de gols na partida {i+1}:")))

dados['Gols'] = lista[:]
dados['Total'] = sum(lista)
print('-=-' * 15)
print(dados)
print('-=-' * 15)
for k, v in dados.items():
    print(f'O campo {k} tem o valor: {v}')
print('-=-' * 15)

print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for i, v in enumerate(dados['Gols']):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f"Foi um total de {dados['Total']}")
