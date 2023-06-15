#Importar funcions per al menu principal.
from curses.ascii import isdigit
#Importar funció per a els numeros aleatoris.
import random
#Importat funcions per a el joc 2D.
import pygame
import juego_2D as juego
#Importam la funció de isdigit per a poder llegir els números del menú.
def menu():
    print("""
            0. Sortir
            1. Aleatori.
            2. Lletres.
            3. Busca minas.
            4. Inicia un objecte fet a blender.
    """)
    a = int(input("Introdueix un número de selecció: "))
    return a

#Genera 50 nombres aleatoris entre 1 al 100.
def aleatori():
    l = []
    for i in range(1,50):
        x = random.randint(1,100)
        l.append(x)
    print(l)

#Introduim el número de vegades que vols escriure lletres o paraules i fiques les lletres/paraules.
def lletres():
    l = []
    for i in range(int(input("¿Cuantas vegaes vols introduir una lletra/paraula?: "))):
        x = (input("Introdueix una lletra/paraula: "))
        l.append(x)
    print(l)

def juego_2D():
    juego.pygame.init()

def objectes():

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
            juego_2D()
        case 4:
            objectes()
        case 0:
            a = False
            print("Adéu, ara sortirem de l'app")
        case other:
            print("Error, opció no vàlida")