#11. Escribir un programa que recibe como parámetros dos horas dadas por horas, minutos y segundos
# e imprime "es anterior" si la primera hora (contemplando horas, minutos y segundos) es anterior que la segunda o "es posterior".
# Resuélvalo de dos maneras: utilizando if y utilizando únicamente expresiones lógicas.

# Se nos pide un programa donde a través de la entrada de dos horas tenemos que si la primera es antes o despues que la segunda.

"""
print("Introduzca en el programa sus datos de la primera hora: \n")
horas_1 = int(input("Cantidad de horas:\n"))
minutos_1 = int(input("Cantidad de minutos:\n"))
segundos_1 = int(input("Cantidad de segundos:\n"))
print("Introduzca en el programa sus datos de la segunda hora: \n")
horas_2 = int(input("Cantidad de horas:\n"))
minutos_2 = int(input("Cantidad de minutos:\n"))
segundos_2 = int(input("Cantidad de segundos:\n"))
print()
if horas_2 != horas_1 and minutos_2 != minutos_1 and segundos_2 !=segundos_1:
    if( horas_1>horas_2):
        print("La primera es despues")
    elif(minutos_1>minutos_2):
        print("La primera es despues")
    elif(segundos_1>segundos_2):
        print(" La primera es despues")
    else:
        print("La segunda hora es más pequeña o igual")
else:
    print("Se tratan de la misma hora")
    """
horas_1 = int(input("Cantidad de horas:\n"))
minutos_1 = int(input("Cantidad de minutos:\n"))
segundos_1 = int(input("Cantidad de segundos:\n"))
print("Introduzca en el programa sus datos de la segunda hora: \n")
horas_2 = int(input("Cantidad de horas:\n"))
minutos_2 = int(input("Cantidad de minutos:\n"))
segundos_2 = int(input("Cantidad de segundos:\n"))

tiempo_total_1= horas_1*60**2+minutos_1*60+segundos_1
tiempo_total_2= horas_2*60**2+minutos_2*60+segundos_2

print()
if tiempo_total_1> tiempo_total_2:
    print('Posterior')
elif tiempo_total_1< tiempo_total_2:
    print('Anterior')
else:
    print('Misma hora')