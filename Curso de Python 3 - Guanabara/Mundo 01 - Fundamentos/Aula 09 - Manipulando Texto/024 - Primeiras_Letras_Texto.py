# 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# 024: Create a program that reads a city name and tells you whether or not it starts with the name "SANTO"

cidade = str(input("Digite o nome da cidade: ")).capitalize().strip()

divide = cidade.split()

print('Santo' in divide[0])
