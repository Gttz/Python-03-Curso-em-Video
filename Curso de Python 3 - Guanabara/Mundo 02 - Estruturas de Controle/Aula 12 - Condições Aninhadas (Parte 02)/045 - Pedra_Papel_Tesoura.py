# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
# Exercise Python 045 : Create a program that makes the computer play Jokenpô with you.
from time import sleep
from termcolor import colored, cprint
from random import choice
lista = [1, 2, 3]

print(colored("-=-", 'red') * 10)
print(colored("Welcome to the game JO-KEN-PÔ!", 'yellow'))
print(colored("-=-", 'red') * 10)

print(colored("I choose my play...", 'cyan'))
sleep(1)
ComputerPlay = choice(lista)
print(colored("Your turn, Choose your move:\n"
              "[1] Rock\n"
              "[2] Paper\n"
              "[3] Scissor", 'green'))
YourPlay = int(input(colored("Your Choose:", 'cyan')))
print(colored("Computer Choice: {}", 'red').format(ComputerPlay))
print(colored("-=-", 'yellow') * 5)
print(colored("Calculating...", 'green'))
print(colored("-=-", 'yellow') * 5)
sleep(1)
if ComputerPlay == YourPlay:
    print(colored("IT'S A DRAW!", 'yellow'))
elif YourPlay == 1 and ComputerPlay == 2:
    print(colored("Your Play Rock and Computer Play Paper...", 'cyan'))
    print(colored("Computer WIN!", 'red'))
elif YourPlay == 2 and ComputerPlay == 3:
    print(colored("Your Play Paper and Computer Play Scissor...", 'cyan'))
    print(colored("Computer WIN!", 'red'))
elif YourPlay == 3 and ComputerPlay == 1:
    print(colored("Your Play Scissor and Computer Play Rock...", 'cyan'))
    print(colored("Computer WIN!", 'red'))

elif YourPlay == 1 and ComputerPlay == 3:
    print(colored("Your Play Rock and Computer Play Scissor...", 'cyan'))
    print(colored("Your WIN!", 'green'))
elif YourPlay == 2 and ComputerPlay == 1:
    print(colored("Your Play Paper and Computer Play Rock...", 'cyan'))
    print(colored("Your WIN!", 'green'))
elif YourPlay == 3 and ComputerPlay == 2:
    print(colored("Your Play Scissor and Computer Play Paper...", 'cyan'))
    print(colored("Your WIN!", 'green'))

