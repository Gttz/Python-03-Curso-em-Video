frase = '    Curso em Video em Python                  '
print('Curso' in frase)  # procura a palavra 'Curso' na frase
print(len(frase))  # mostra o tamanho da frase
print(frase.find('som'))  # procura a palavra 'som' na frase (True,False)

print(frase.replace('Video', 'som'))  # troca uma palavra por outra e apenas printa
# frase = print(frase.replace('Video', 'Som'))  troca a PALAVRA por outra na mémoria
# print(frase)

print(frase.upper())  # deixa tudo em caps
print(frase.lower())  # deixa tudo sem caps
print(frase.capitalize())  # deixa só a primeira letra em caps
print(frase.title())  # Transforma todos começo de frase em minusculo
print(frase.strip())  # remove todos os espaços da esquerda e da direita
print(frase.lstrip())  # remove espaços da esquerda
print(frase.rstrip())  # remove espaços da direita

print(frase.count('o'))  # Conta quantas vezes apareceu a letra 'o'
# print(frase.find('o'))  # mostra onde a primeira letra 'o' foi encontrada
# print(frase.lfind('o'))  # mostra onde a letra 'o' do lado esquerdo(l = left) foi encontrada
# print(frase.rfind('o'))  # mostra onde a letra 'o' do lado direito(r = right) foi encontrada

frase2 = 'Curso em Video em Python'

print(frase2.split())  # divide a frase em sub-vetores e os printa
dividido = frase2.split()
print(dividido[0][-1])  # com apenas o [0], mostra a primeira palavra e com [-1] mostra o final da frase
print('-'.join(frase2))  # coloca '-' nos espaços digitados ( não deu muito certo)

# No python não tem tipo char, para pegarmos apenas a primeira letra usamos [0] que apenas a primeira posição Exemplo:
sexo = str(input("Digite o sexo [M]/[F]: "))[0].capitalize().strip()
