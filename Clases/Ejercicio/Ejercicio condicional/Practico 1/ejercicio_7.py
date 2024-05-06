"""7. Escribir un programa que permita determinar si un año es bisiesto utilizando la estructura condicional."""

"""Todos los años bisiestos son divisibles entre 4.
Aquellos años que son divisibles entre 4, pero no entre 100, son bisiestos.
Los años que son divisibles entre 100, pero no entre 400, no son bisiestos.
Sin embargo, los años divisibles entre 100 y entre 400 sí que son bisiestos"""

año=int(input("Introduzca el año:\n"))
if(año % 4 !=0):
    print("No es bisiesto")
elif(año % 100 !=0):
   print("No es bisiesto")
elif(año %400 !=0):
    print("No es bisiesto")
else:
    print("Es bisiesto")