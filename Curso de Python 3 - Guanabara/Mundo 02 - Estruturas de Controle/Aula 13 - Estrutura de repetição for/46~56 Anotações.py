for i in range(0, 6):  # normal ( do 0 ao 5, lembrando que o último número(6) não é contado)
    print(i)

for j in range(6, 0, -1):  # de trás pra frente
    print(j)

for k in range(0, 11, 2):  # pulando de 2 em 2 (0 ao 10)
    print(k)

for l in range(0, 16, 3):  # pulando de 3 em 3 (0 ao 15)
    print(l)
print("-=-" * 6)
n = int(input("Digite um número:"))
for m in range(0, n+1):  # vai até onde oque o usuário digitou.
    print(m)
print("-=-" * 6)
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
for n in range(inicio, fim, passo): # pede os 3 comandos para o usuário e os executa.
    print(n)
print("-=-" * 3)