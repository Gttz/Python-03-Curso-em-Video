# Tuplas são imultáveis , não dá para trocar os elementos depois de feitos.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', "Batata Frita")
#lanche[1] = 'Chocolate' # - deu erro porquê não podemos muda-lo.
# 1:3 Acessa o elemento 1 que é Suco até a Pizza, lembrando que o último elemento não é contado
print(lanche[1:3])

# -1 para acessar o último elemento , -2 para penúltimo e assim retrocedendo.
print(lanche[-1])

# vai do 2 até o final
print(lanche[2:])

# acessa todos os elementos menos o 3 e o 4
print(lanche[:3])

# Há dois jeitos de fazer com for
# Nós podemos começar do 0 e ir até o tamanho do vetor
for i in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[i]}")
#Ou podemos ir direto ao fim do tamanho do lanche com 'in lanche'
for comida in lanche:
    print(f"Eu vou comer {comida}")

# Forma de mostrar oq é o elemento e onde ele está
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

#Mostra os elementos ordenados alfabeticamente
print(sorted(lanche))
