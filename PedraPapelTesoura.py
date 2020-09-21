from random import randint

t = ["Pedra", "Papel", "Tesoura"]

computer = t[randint(0,2)]

player = False

while player == False:

    player = input("Pedra, Papel, Tesoura?")
    if player == computer:
        print("Empatado!")
    elif player == "Pedra":
        if computer == "Papel":
            print("Perdeste!", computer, "envolve", player)
        else:
            print("Ganhaste!", player, "esmaga", computer)
    elif player == "Papel":
        if computer == "Tesoura":
            print("Perdeste!", computer, "corta", player)
        else:
            print("Ganhaste!", player, "envolve", computer)
    elif player == "Tesoura":
        if computer == "Pedra":
            print("Perdeste...", computer, "esmaga", player)
        else:
            print("Ganhaste!", player, "corta", computer)
    else:
        print("Jogada inválida. Por favor tenta novamente!")
    player = False
    computer = t[randint(0,2)]