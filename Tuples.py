a=[1,2,3]
b= tuple(a)
x,y,z = b
print("x=",x,"y=",y,"z=",z)

for e in b:
    print(e)

for i in range(len(b)):
    print(i)

for i,e in enumerate(b):
    print ("Posició:",i,"Valor:",e)
