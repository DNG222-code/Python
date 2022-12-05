def el_
paraula = input("Ingresi una paraula: ")
paraula_al_reves = paraula[::-1]
if( paraula == paraula_al_reves ):
    print("Es palindrom")
else:
    print("No es palindrom")