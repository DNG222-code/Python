def invertit (a):
    b = list(a)
    c = b[::-1]
    r = "".join(c)
    return r

#PP
a = input("Escriu una paraula: ")
b = invertit (a)
print ("La paraula", a, "i guarda és ", b)