def menu_principal()

opcio=1
while(opcio!=0):
    print("""Calculadora
        Menú:
        1. Números enters
        2. Números reals
        3. Canvis de base
        0. Sortir
    """)
    opcio=input("Seleccioni l'opció que vulgui: ")
    match opcio:
        case "1":
            print("""
            Menú calculadora de números enters:
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            0. Sortir
            """)
            opcio2=input("Seleccioni l'opció que vulgui: ")
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))
            match opcio2:
                case "1":
                    c=a+b
                    print("La suma de ",a," més ",b," és ",c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menys ",b," és ",c)
                case "3":
                    c=a*b
                    print("La multiplicació de ",a," per ",b," és ",c)
                case "4":
                    c=a/b
                    print("La divisió de ",a," per ",b," és ",c)
                case "0":
                    print("Adéu")
                case other:
                    print("Opció no vàlida!")
        case "2":
            print("""
            Menú calculadora de números reals:
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            0. Sortir
            """)
            opcio2=input("Seleccioni l'opció que vulgui: ")
            a = float(input("Indiqui el primer operand: "))
            b = float(input("Indiqui el segon operand: "))
            match opcio2:
                case "1":
                    c=a+b
                    print("La suma de ",a," més ",b," és ",c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menys ",b," és ",c)
                case "3":
                    c=a*b
                    print("La multiplicació de ",a," per ",b," és ",c)
                case "4":
                    c=a/b
                    print("La divisió de ",a," per ",b," és ",c)
                case "0":
                    print("Adéu")
                case other:
                    print("Opció no vàlida!")
        case "3":
            print("""
            Menú calculadora canvis de base:
            1. Donat un binari passar a octal, decimal i hexadecimal.
            2. Donat un octal passar a binari, decimal i hexadecimal.
            3. Donat un decimal passar a binari, octal i hexadecimal.
            4. Donat un hexadecimal passar a binari, octal i decimal.
            0. Sortir
            """)
            opcio2=input("Seleccioni l'opció que vulgui: ")
            a = input("Indiqui el número a convertir: ")
            match opcio2:
                case "1": # Binari a
                    b=int(a,base=8)
                    c=int(a,base=10)
                    d=int(a,base=16)
                    print("El número ",a," en octal= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "2": # Octal a
                    b=int(a,base=2)
                    c=int(a,base=10)
                    d=int(a,base=16)
                    print("El número ",a," en binari= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "3": # Decimal a
                    b=int(a,base=2)
                    c=int(a,base=8)
                    d=int(a,base=16)
                    print("El número ",a," en binari= ",b, " en octal= ",c," en hexadecimal= ", d)
                case "4": # Hexadecimal a
                    b=int(a,base=2)
                    c=int(a,base=8)
                    d=int(a,base=10)
                    print("El número ",a," en binari= ",b, " en octal= ",c," en decimal= ", d)
                case "0":
                    print("Adéu")
                case other:
                    print("Opció no vàlida!")
        case "0":
            print("Adéu")