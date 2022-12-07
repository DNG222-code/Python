def crear_repetits(a,b):
    c = b*int(a)
    return c
a = input ("Introdueixi num. repeticions: ")
b = input ("Introdueixi un carácter a repetir")
print ("El caracter ", b, " repetit", a,"vegades, és: ",crear_repetits(a,b))
