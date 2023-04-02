import random

def calculam_n_aleatoris():
    b = []
    for i in range(4):
        b.append(random.randint(0, 9))
    return b

def llegir_n_usuari():
    b = []
    for i in range(4):
        b.append(int(input("Introdueix un número: ")))
    return b

def comparar(a, b):
    totigual = 0
    existeixen = 0
    for i in range(4):
        if a[i] == b[i]:
            totigual += 1
        elif b[i] in a:
            existeixen += 1
    return totigual, existeixen

a = calculam_n_aleatoris()
b = llegir_n_usuari()
sortir = 0

while sortir != 1:
    x, y = comparar(a, b)
    b = llegir_n_usuari()
    if x == 4:
        print("Has encertat tots els números {}".format(b))
        sortir = 1
    elif x < 4 and y > 0:
        print("Has encertat {} números i n'hi ha {} que hi són però no són al seu lloc".format(x, y))
    elif x < 4 and y == 0:
        print("No has adivinat res")
    elif x == 0 and y > 0:
        print("No has adivinat res")
    elif x == 0 and y == 0:
        print("Has encertat {} números i n'hi ha {} que hi són però no són al seu lloc".format(x, y))