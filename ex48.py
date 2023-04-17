def crear_lista_fixer(fitxernou):
    with open(fitxernou, 'r') as f:
        l = f.readlines()
        lineaparaules = [linea.rstrip('\n')for linea in l]
        print(lineaparaules)
        f.close()

crear_lista_fixer('/home/alumnat/Escritorio/fitxernou.txt')