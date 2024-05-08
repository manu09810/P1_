#10. Escribir un programa que reciba una fecha dada por tres números (día, mes y año)
# e indica si es una fecha valida. Tener en cuenta que los meses de Enero, Marzo, Mayo,
# Julio, Agosto, Octubre y Diciembre tienen 31 días, Febrero 28 (o 29 días si es bisiesto)
# y el resto de los meses 30 días.
dia=int(input("Ingrese la fecha del día \n"))
mes=int(input("Ingrese la fecha del mes \n"))
año=int(input("Ingrese el año\n"))
bisiesto= False

if mes == 2:
    if (año % 4 == 0):  # Código para ver que tipo de año es.
        bisiesto = True
    elif (año % 100 == 0 and año % 400 == 0):
        bisiesto = True

if((mes == 4 or mes == 6 or mes == 9 or mes ==11) and dia<=30):
    print("La fecha es correcta")
elif ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)and dia<=31):
    print("La fecha es correcta")
elif(mes == 2 and bisiesto == False and dia<=28):
    print("No se trata de un año bisiesto y es valido")
elif(mes == 2 and bisiesto == True and dia<=29):
    print("Se trata de un año bisiesto y es valido")
else:
    print("Algo esta mal")