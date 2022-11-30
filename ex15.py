#Funció sumar elements de la llista
def sumar_llista(a):
    sumatori = 0
    for i in a:
        sumatori += i
    return sumatori
#Funció multiplicar elements de la llista
def multiplicar_lista (lista):
    multiplicado=1
    for x in lista:
        multiplicado*= x
    return multiplicado

#Programa principal
x = [1,3,4,5,7]
print ("El sumatori és: ", sumar_llista(x))
print("La multiplicació és de: ", multiplicar_lista(x))