def monstri(i):
    l = []
    for e in range(i, 0, -1):
        l.append(e)
    print(''.join(map(str, l)))

# Programa

x = int(input("Introdueixi un número diminut: "))
for i in range(x, 0, -1):
    monstri(i)