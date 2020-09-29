# 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao tudo (sem considerar espaços).
# - Quantas letras tem o primeiro nome

#Exercise 022: Create a program 'that reads a person's' full name and 'show':
# - The name 'with' all 'uppercase and lowercase letters'
# - 'How many letters to' all ('without considering spaces')
# - 'How many letters has' the first name

NomeCompleto = input("Digite o seu nome completo:").strip()

print("O nome com todas as letras maiúsculas e minúsculas:"
      "\nMaiúsculas:", NomeCompleto.upper(),
      "\nMinúsculas:", NomeCompleto.lower())

print("Quantas letras ao todo (sem considerar espaços):", len(NomeCompleto) - NomeCompleto.count(' '))

Dividido = NomeCompleto.split()
print("Quantas letras tem o primeiro nome:", len(Dividido[0]))
