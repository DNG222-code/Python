"""
1
x = int(input("Introdueixi un número: "))
if x % 2 == 0:
    print("El número {} és parell". format(x))
else:
    print("El número {} és senar".format(x))
2
x = int(input("Introdueixi un número: "))
if x > 10:
    print("El número {} és major". format(x))
else:
    print("El número {} és menor".format(x))
"""

"""
3
def llegir():
    a = 'b'
    l = []
    while a != '.':
        a = input("Introdueix un número: ")
        if a!= '.':
            l.append(int(a))
        return l
def comparar(a,c):
        for e in a:
            if e>c:
                print(e)

#Programa principal
x = llegir()
y = input("Introdueixi el número a comparar: ")
comparar(x,y)
"""

4
def menu():
    print("""
    Calculadora de números enters
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Potència
    0. Sortir
    """)

    x = input("Introdueixi l'opció desitjada")
    return int(x)

def llegir_valors():
    a = input("Introdueixi el primer vlaor: ")
    b = input("Introdueixi el segon valor: ")
    return int(a), int(b)

#Programa principal
opcio = 10
while opcio!=0:
    opcio=menu()
    if opcio!=0:
        match opcio:
            
