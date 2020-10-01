a = (2, 5, 4)
b = (5, 8, 1, 2)
#Podemos juntar duas tuplas:
c = a + b
print(c)
# conta quantas vezes um número se repetiu, caso tenha dois números ele pega a primeira ocorrência que encontrou
print(c.count(5))
#procura o elemento digitado, caso tenha dois números ele pega a primeira ocorrência que encontrou
print(c.index(2))
# Ordena os elementos em ordem
print(sorted(c))

#Diferente do java, podemos colocar diferentes valores nas tuplas:
pessoa = ('Lucas', 21, 'M', 81.99)
print(pessoa)