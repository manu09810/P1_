"""1. Leer números desde teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de
todos los números positivos ingresados (solo de los números que sean positivos).
"""
n=""
sumatoria=0
while (n!=0):
    n = int(input("Introduzca números\n"))
    if n>0:
        sumatoria=sumatoria+n
print(sumatoria)