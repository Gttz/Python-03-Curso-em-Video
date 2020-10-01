# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

brasileirao = ('Atlético', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense', 'America-MG', 'Sao Paulo', 'Grêmio',
               'Vasco da Gama', 'Internacional', 'Botafogo', 'Sport', 'Recife', 'Cruzeiro', 'EC Vitoria', 'Santos',
               'Chapecoense', 'Atlético-PR', 'Bahia', 'Ceará', 'SC', 'Paraná')

print(f"Os cinco primeiros times do brasileirão são: {brasileirao[0:5]}")
print(f"Os quatro últimos colocados do brasileirão são: {brasileirao[-4:]}")
print(f"Os times em ordem alfabética do brasileirão são: {sorted(brasileirao)}")
print(f"O time da Chapecoense do brasileirão está na posição: {brasileirao.index('Chapecoense')}")


