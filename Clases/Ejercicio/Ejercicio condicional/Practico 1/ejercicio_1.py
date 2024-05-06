"""
1. Escribir un programa que implemente el valor absoluto (pero sin usar la función provista por python).
Nota: para los números positivos su valor absoluto es igual al número
 (ej: el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
"""
n= int(input("Ingrese el valor de n \n"))
if n<0:
    n=n*-1
print("El valor absoluo de n es:\n",n)