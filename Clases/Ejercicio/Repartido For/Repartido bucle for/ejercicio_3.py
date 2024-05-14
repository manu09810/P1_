# 3. Escribir un programa que permita al usuario ingresar 6 números enteros,
# que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los
# números negativos y el promedio de los positivos. No olvides que no es posible dividir por cero,
# por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.
sum_negativo = 0
sum_positivo = 0
divisor = 0
for i in  range (6):
    n = int(input('Introduzca N:\n'))

    if n > 0:
        sum_positivo = sum_positivo + n
    else:
        sum_negativo = sum_negativo + n
    print(i)
promedio = sum_positivo/6
print()
print(sum_negativo)
print(promedio)





