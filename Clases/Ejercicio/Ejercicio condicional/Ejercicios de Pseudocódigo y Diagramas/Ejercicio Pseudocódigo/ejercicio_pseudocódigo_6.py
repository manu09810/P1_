"""6) La empresa MiTienda cobra sus envíos según el peso de los productos. En los
envíos para Uruguay, la tarifa es de 21.99 US$ por kg. La empresa ofrece un 30% de
descuento a partir del 3kg y un 50% de descuento a partir del 5kg. Escriba un
algoritmo en pseudocódigo que dado el peso indique el monto a pagar."""
tarifa = 22 #Lo puse 22 en vez de 21.99 por lo estetico.
coste = 0
peso = int(input("Peso del paquete:\n"))
if(peso > 5):
    coste = (tarifa * 0.5)*peso
elif(peso > 3):
    coste = (tarifa * 0.7) * peso
else:
    coste = tarifa * peso
print("El monto a pagar es: \n",str(coste) )