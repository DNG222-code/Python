def menu(a):
    print("""
        Menu
        1.Dibuix1
        2.Dibuix2
        3.Sortir
        """)
    opcio:input("Seleccioni el dibuix que vulgui: ")
    return opcio

def crear_punts(a):
    match(a):
        case "1":
            print(""" .
             . .  
             .   .
              . .
              .
              """)
        case "2":
            print(""" _
            | | |
            _ _
             | | |
             _ _
             """)
        case other:
            print("Adéu")

opcio=2
while(opcio)