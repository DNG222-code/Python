def suma_de_dos_digits():
    x = float(input("Introdueix un numero: "))
    z = float(input("Introdueix un altre numero: "))
    suma = x + z
    print("La suma de", x, "i", z, "es:", suma)
    
    # Compara la suma con 0 para determinar si es par o impar
    if suma % 2 == 0:
        print("La suma es parella.")
    else:
        print("La suma es senar.")

# Ejecutar la función
suma_de_dos_digits()