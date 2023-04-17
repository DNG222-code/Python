def llegir_paraules():
    a = []
    b = ""
    while b != ".":
        b = input("Introdueixi una paraula: ")
        if b != ".":
            a.append(b)
    a.sort()
    return a

def index_paraula(llista, paraula):
    return [i for i, element in enumerate(llista) if paraula == element]

#Programa

a = llegir_paraules()
x = input("Introdueix la paraula: ")
b = index_paraula(a,x)
if len(b) == 0:
    print("A la llista {} no hi ha l'element {}".format(a,x))
else:
    print("A la llista {} la paraula {} apareix {} vegades en les següents posicions: {}".format(a,x, len(b),b))