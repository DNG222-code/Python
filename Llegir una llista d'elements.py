def llegir_llista():
    l = []
    for i in range(10):
        l.append(input())
    return l

x = llegir_llista()
numM = 0
for e in x:
    if e[0] == "M":
        numM += 1
print("Hg", "numM,")
