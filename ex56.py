def primer(numeros):
    if numeros < 2:
        return False
    for i in range(2, numeros):
        if numeros % i == 0:
            return False
    return True

# Programa

numerosprimers = 0
l = []
for numeros in range(1, 101):
    if primer(numeros):
        l.append(numeros)
        numerosprimers += 1
print("Hi ha {} números primers i són {}".format(numerosprimers, l))