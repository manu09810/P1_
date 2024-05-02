"""i=1
suma=0
while(i!=0):
    i=int(input("Ingrese su n\n"))
    suma=suma+i
suma= suma-1
print("La suma total es: \n",str(suma))"""

acumulador=9
Salir=False
while salir:
    m= int(input("Ingrese um número"))
    if m==0:
        salir=True
    else:
        acumulador= acumulador+m
print("La suma es:", acumulador) #no es necesario usar str si se pone ´,´