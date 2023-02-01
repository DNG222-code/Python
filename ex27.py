def llegir_llista():
    ll = []
    for i in range(4):
        v = []
        v.append (input("Introdueixi el nom:"))
        v.append (input("l'any de naixement "))
        ll.append(v)
    return ll

# Progrma inicial

a = llegir_llista()
print()
