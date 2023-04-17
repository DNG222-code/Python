def sumar(a, b):
    sum = 0
    if a > b:
        for i in range(b, a+1, 1):
            sum += i
    elif b > a:
        for i in range(a, b+1, 1):
            sum += i
    else:
        sum = 0
    return sum

#Programa

a = int(input("Introdueix primer número: "))
b = int(input("Introdueix segon número: "))
c = sumar(a, b)
print("La suma dels números entre {} i {} és {}".format(a, b, c))