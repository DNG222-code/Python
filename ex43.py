def lista():
    l = []
    letra = "a"
    while letra!=".":
        letra = input("Introduzca un elemento de la lista i un punto(.) para acabar:");
        if letra!=".":
            l.append(letra)
        return l

def eliminar_capicua(a):
    b = []
    if len(a)>2:
        b = a[1:-1]
    return b

x = lista()
y = eliminar_capicua(x)
print("La llista original {} s'ha transformat en la llista {}".format(x,y));