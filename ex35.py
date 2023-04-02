def llegir_paraula():
    return(input("Introduir una paraula: "))
def comparar_paraules(a,b):
    if a == b:
        print("Són iguals, per tant rimen")
    elif a[-3:] == b[-3:]:
        print("Rimen, per que les 3 dames lletres són iguals")
    elif a [-2:] == b[-2:]:
        print("Rimen, un poc, 2 dames lletres són iguals")
    elif a [-1:] == b[-1:]:
        print("No rimen")
a = llegir_paraula()
b = llegir_paraula()
comparar_paraules(a,b)