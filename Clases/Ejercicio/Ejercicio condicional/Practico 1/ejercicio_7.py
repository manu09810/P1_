"""
7. Escribir un programa que permita determinar si un año es bisiesto utilizando la estructura condicional.
"""
año=int(input())
if(año % 4 ==0):
    print("Es bisiesto")
elif(año % 100 ==0 and año % 400 ==0):
    print("Es bisiesto")
else:
    print("No es bisiesto")