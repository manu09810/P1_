"""8. Escribir un programa que lea el día de la semana (en número entero, donde 1 corresponde a lunes y 7 a domingo) e imprima el siguiente mensaje:
-  si es lunes imprima “Hoy comienza la semana. Animo!”,
-  si es viernes “Ya casi termina!”
-  si es sábado o domingo “Siiii! Fin de semana!”
-  si el día ingresado no es ninguno de esos (pero es válido), imprimir el siguiente mensaje “Vamos que se puede!”
-  si el día ingresado no es válido entonces debe mostrar un cartel que lo indique"""
print('\nCada día se representa con un n, desde el 1(lunes) hasta el 7(domingo)')
dia_en_teclado= int(input("Introduce tu día:\n"))

if dia_en_teclado == 1:
    print('Hoy comienza la semana. Animo!')
elif (dia_en_teclado == 2 or dia_en_teclado == 3 or dia_en_teclado == 4):
    print('Vamos que se puede carajo!!!')
elif dia_en_teclado == 5:
    print('Ya casi termina')
elif (dia_en_teclado == 6 or dia_en_teclado == 7):
    print('Sii, fin de semana')
else:
    print('El valor no es valido')