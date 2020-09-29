# 027: Faça um programa que leia o nome completo de uma pessoa,
#      mostrando em seguida o primeiro e o último nome separadamente.

NomeCompleto = str(input("Digite o nome completo: ")).strip()

Divide = NomeCompleto.split()

print("Primeiro nome: ", Divide[0], "\nÚltimo nome:", Divide[-1])
