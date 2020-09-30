nome = str(input("Digite o seu cargo:")).strip().capitalize()

if nome == 'Dono':
    print("Olá {} todo poderoso pika das galáxias!".format(nome))
elif nome == 'Gerente':
    print("Olá {}, em quem você quer mandar hoje?".format(nome))
elif nome == 'Senior' or nome == 'Pleno' or nome == 'Junior':
    print("Olá funcionário {}, vá trabalhar AGORA!".format(nome))
elif nome == 'Estagiario':
    print("Olá {}, vá encher o saco dos funcionários.".format(nome))
else:
    print("Você ao menos passou na entrevista?")
