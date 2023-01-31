#Definir una funció que donada una llista de paraules i un número x, retorni totes les paraules que tingui més d'x caràcters.

def filtrar_paraules(a, num):
    b = list()
    i = 0
    for e in a:
        if num < len(e):
            b.append(e)
            return b

x = ["hola","Sí", "Un senyor damunt un ruc", "filòsof", "Xouman", "Prototip"]
a = input("indica la longitud de les paraules que vols filtrar: ")
y = filtrar_paraules(x,int(a))
print("Les paraules de igual o més tamany de ",a,"són: ", y)