opcio=1
while(opcio!=1):
    print ("""Calculadora
    Menú:
    1. Números enters
    2. Numeros reales
    3. Canvi de base
    0. Sortir
""")
opcio=input("Seleccioni l'opció que vulgui: ")
match opcio:
    case "1":
        print ("""
        Menú:calculadora de números enters:
        1. Suma
        2. Resta
        3. Multiplica
        4. Dividir
        0. Sortir
        """)
a = input("Indiqui el primer operand: ")
b = input("Indiqui el segon operand: ")
match opcio:
    case "1":
        c=int(a)+int(b)
        print("La suma de ",a," més ",b," és ",c,"")
    case "2":
        c=int(a)-int(b)
        print("La resta de ",a," menys")
    case "3":
        c=int(a)*int(b)
        print("La multiplicació de ",a," per ",b,"és ",c)
    case "4":
        c=int(a)/int(b)
        print("La divisió de ",a," per ",b," és ",c)
    case "0":
        print("Opció no valida")
