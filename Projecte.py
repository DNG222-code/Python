from curses.ascii import isdigit
import random
#Importam la funció de isdigit per a poder llegir els números del menú.
def menu():
    print("""
            0. Sortir
            1. Aleatori.
            2. Lletres.
            3. Inicia un objecte fet a blender.
            4. Busca minas.
    """)
    a = int(input("Introdueix un número de selecció: "))
    return a

#Genera 50 nombres aleatoris entre 1 al 100
def aleatori():
    l = []
    for i in range(1,50):
        x = random.randint(1,100)
        l.append(x)
    print(l)

def lletres():
    l = []
    for i in range(int(input("¿Cuantas vegaes vols introduir una lletra?: "))):
        x = (input("Introdueix una lletra: "))
        l.append(x)
    print(l)

def objectes():
    print("He passat per objectes")    

def cercar_mines():
    print("He passat per cercar mines") 

#programa principal
a = True
while a:
    a = menu()
    match a:
        case 1:
            aleatori()
        case 2:
            lletres()
        case 3:
            objectes()
        case 4:
            cercar_mines()
        case 0:
            a = False
            print("Adéu, ara sortirem de l'app")
        case other:
            print("Error, opció no vàlida")