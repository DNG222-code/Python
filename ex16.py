def invertit (a):
    b = list(a)
    c = b[::-1]
    r = str(c)
    return r

a = input("Escriu una paraula: ")
b = invertit (a)
print ("La paraula", a, "i guarda és ", b)