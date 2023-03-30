import random

sorteio = random.randint(2,9)
print("=="*30)
print("O número sorteado foi", sorteio)

if sorteio >=5:
    print(sorteio, "X", 1, "=", sorteio*1)
    print(sorteio, "X", 2, "=", sorteio*2)
    print(sorteio, "X", 3, "=", sorteio*3)
    print(sorteio, "X", 4, "=", sorteio*4)
    print(sorteio, "X", 5, "=", sorteio*5)
    print(sorteio, "X", 6, "=", sorteio*6)
    print(sorteio, "X", 7, "=", sorteio*7)
    print(sorteio, "X", 8, "=", sorteio*8)
    print(sorteio, "X", 9, "=", sorteio*9)
    print(sorteio, "X", 10, "=", sorteio*10)

else:
    print(sorteio, "X", 10, "=", sorteio*10)
    print(sorteio, "X", 9, "=", sorteio*2)
    print(sorteio, "X", 8, "=", sorteio*8)
    print(sorteio, "X", 7, "=", sorteio*7)
    print(sorteio, "X", 6, "=", sorteio*6)
    print(sorteio, "X", 5, "=", sorteio*5)
    print(sorteio, "X", 4, "=", sorteio*4)
    print(sorteio, "X", 3, "=", sorteio*3)
    print(sorteio, "X", 2, "=", sorteio*2)
    print(sorteio, "X", 1, "=", sorteio*1)
 