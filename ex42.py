suma = 0
numero = input("Introdueix un número: ");
print("{} té {} dígits".format(numero,len(numero)));
for i,e in enumerate(numero):
	if i%2==0:
		print("El número parell {} és {}".format(i,e));