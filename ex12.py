# Definició de funcions
def gran_de_tres(x,y,z):
    a=x
    if(x>y):
        if(x>z):
            a = x
        elif (z>x):
            a = z
        else:
            a = x
    elif (y>x):
        if (y>z):
            a = y
        elif (z>y):
            a = z
        else: #
            