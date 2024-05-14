## 1. Escribir un programa que solicite
# al usuario una cantidad y luego itere la cantidad de veces dada.
# En cada iteración, solicitar al usuario que ingrese un número.
# Al finalizar, mostrar la suma de todos los números ingresados.

n = int(input('introduce num '))
acumulador = 0
for i in range(n):
    pedir_num = int(input(''))
    acumulador = pedir_num + acumulador
    print(i)
print(acumulador)