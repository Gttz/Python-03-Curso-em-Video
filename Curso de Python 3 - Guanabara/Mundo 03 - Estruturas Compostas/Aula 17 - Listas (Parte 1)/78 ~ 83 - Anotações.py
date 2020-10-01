# podemos criar uma lista assim:
lista = [2, 5, 9, 1]
# Ou assim, porém não podemos adicionar os valores ali, é melhor usada caso esteja inicialmente vazia e depois nós
# adicionarmos aos poucos
lista2 = list()
# para mudar um número
lista[2] = 2
# para adicionar um elemento na última posição
lista.append(7)
# adiciona um elemento em determinada posição(posição [2] = 25)
lista.insert(2, 25)
print(lista)
# Remove um elemento na primeira posição que encontrar
lista.remove(2)
print(lista)
# Caso queiramos remover um elemento que não está na lista, devemos usar um if antes para verificar:
if 4 in lista:
    lista.remove(4)
    print(lista)
else:
    print('Não achei o número 4')
# Remove um elemento em determinada posição(posição [2] = null
lista.pop(2)
print(lista)
# --------------------Ordenações----------------------
print('-=-' * 13)
print('ordena todos os valores')
lista.sort()
print(lista)
print('ordena todos os valores ao contrário')
lista.sort(reverse=True)
print(lista)
print('-=-' * 13)
# ----------------------------------------------------
# Mostra quantos elementos há na lista
print(f"Essa lista tem {len(lista)} elementos")
print('-=-' * 13)
# ----------------------------------------------------
print('Formas de usar o FOR com a lista:')
valores = list()
valores.append(5)
valores.append(3)
valores.append(4)
valores.append(2)

# Mostra os valores dentro da lista com o FOR
for v in valores:
    print(f"{v}...")
# Mostra a posição e os valores dentro da lista com o FOR e com o comandos enumerate
for p, v in enumerate(valores):
    print(f'Na posição {p} encontrei o valor {v}')

valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input("Digite um valor: ")))
print(f'Os elementos adicionados na lista "valores 2" são: {valores2}')
print('-=-' * 13)

a = [2, 3, 4, 7]
# Liga a lista B com a lista A
b = a
# A lista B recebe todos os valores da lista A
b = a[:]
b[2] = 8
print(a)
print(b)
