def any(any):
    if any%4==0 and any%100==0 or any%400>0:
        print("Es un any de traspas ");
    else:
        print("{} no es un any de traspas ");

x = int(input("Introdueix un any: "));
any(int(x))