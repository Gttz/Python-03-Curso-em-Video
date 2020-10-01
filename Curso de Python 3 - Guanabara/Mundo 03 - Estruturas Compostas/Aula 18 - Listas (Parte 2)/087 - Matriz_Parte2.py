# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
soma = somat = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o elemento da [{l}],[{c}]: "))

for l in range(0, 3):
    somat += matriz[l][2]
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print(f"A soma de todos os valores pares digitados é de: {soma}")
print(f"A soma de todos os valores da terceira coluna é de: {somat}")
print(f"Oa maior valor da segunda linha é: {max(matriz[1])}")
