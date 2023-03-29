def llegir_numero():
    return(int(input("Introdueix numero:")))

def taula_multiplicar(a):
    for i in range (20):
        print("{} x {} = {}".format(i,a,i*a))

a = llegir_numero()
taula_multiplicar(a)