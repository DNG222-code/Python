def paraula_mes_llarga(a):
    b = list()
    i = 0
    for e in a:
        b[i] = len (e)
    b.sort()
    return b [::-1]

x = ["hola","adeu","Sí","matematiques"]
e = paraula_mes_llarga(x)
print(e[0])
