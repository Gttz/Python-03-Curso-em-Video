# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for i in palavras:
    print(f"\nNa palavra {i.upper()} temos ", end='')
    for letra in i:
        if letra in 'aeiou':
            print(letra, end=' ')
