# Definició de funcions
def longitut(a):
    l = 0
    for i in a:
        l +=1
    return l

# Aplicació principal
a = input("Introdueix una cadena: ")
b = longitut(a)
print("La longitud ", a, "és ", b)
c = list()
x="a"
while (x!='.'):
    x = input("Introdueix el següent element de la llista: ")
    c.append(x)
d = longitut(c)
print("La longitut ", c, "és ", d)