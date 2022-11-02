# Calculadora

print ("""
Menú:
1. Suma
2. Resta
3. Multiplica
4. Dividir
5. Sortir
""")

opcio=input("Seleccioni l'opció uqe vulgui: ")
a = input("Indiqui el primer operand: ")
b = input("Indiqui el segon operand: ")

match opcio:
    case "1":
        c=int(a)+int(b)
        print("La suma de ",a," més " ,b, " és ",c)
    case "2":
        c=int(a)-int(b)
        print("La resta de ",a," menys ",b," és ",c)