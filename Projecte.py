from curses.ascii import isdigit
import random
#Importam la funció de isdigit per a poder llegir els números del menú.
def menu():
    print("""
            0. Sortir
            1. Fica unes coordenades i blender imprimeix un objecte
            2. Adivinar un número.
            3. Inicia un objecte fet a blender.
            4. Busca minas.
    """)
    a = int(input("Introdueix un número de selecció: "))
    return a

def llista():
    print("He passat per la llista")

#Funció per a poder adivinar un número del 0 al 20
def adivina():
    a =[]
    for i in range(random.randint):
        a.append(0,20)
    x = input(int("Esriu un numero que vulguis: "))

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
            llista()
        case 2:
            adivina()
        case 3:
            objectes()
        case 4:
            cercar_mines()
        case 0:
            a = False
            print("Adéu, ara sortirem de l'app")
        case other:
            print("Error, opció no vàlida")