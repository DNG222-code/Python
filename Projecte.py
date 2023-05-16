from curses.ascii import isdigit
#Importam la funció de isdigit per a poder llegir els números del menú.

def menu():
    while True:
        print("""
            0. Sortir
            1. Fica unes coordenades i blender imprimeix un objecte
            2. Adivinar un número.
            3. Inicia un objecte fet a blender.
            4. Busca minas.
    """)
        a = input("Introdueix un número de selecció: ")
        if isdigit(a):
            if int(a) > -1 and int(a) < 5:
                return a

print(menu())

def adivinar_un_menu():
    while 