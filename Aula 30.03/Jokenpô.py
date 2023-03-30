import random

print("Faça sua jogada [1] pedra, [2] papel, [3] tesoura")
jogador = int(input())
print("Vez do computador:")
computador = random.randint(1,3)
print(computador)

if jogador == 1 and computador == 2:
    print("O jogador jogou pedra e o computador jogou papel")
    print("Pc ganhou")
elif jogador == 1 and computador == 3:
    print("O jogador jogou pedra e o computador jogou tesoura")
    print("Jogador ganhou")
elif jogador == 2 and computador == 1:
    print("O jogador jogou papel e o computador jogou pedra")
    print("Jogador venceu")
elif jogador == 2 and computador == 3:
    print("O jogador jogou papel e o computador jogou tesoura")
    print("Pc ganhou")
elif jogador == 3 and computador == 1:
    print("O jogador jogou tesoura e o computador jogou pedra")
    print("Pc ganhou")
elif jogador == 3 and computador == 2:
    print("O jogador jogou tesoura e o computador jogou papel")
    print("Jogador ganhou")
else:
    print("Empate")
