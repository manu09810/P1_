#9. Escribir el mismo programa anterior pero el día de la semana
# se especifica con string (es decir el input leerá el día de la semana en letras, por ejemplo “lunes”).
# Tenga en cuenta que algunos controles podrían cambiar.

print('\nCada día se representa con un n, desde el 1(lunes) hasta el 7(domingo)')
dia_en_teclado= input("Introduce tu día:\n")

if dia_en_teclado == "lunes":
    print('Hoy comienza la semana. Animo!')
elif (dia_en_teclado == 'martes' or dia_en_teclado == 'miercoles' or dia_en_teclado == 'jueves'):
    print('Vamos que se puede carajo!!!')
elif dia_en_teclado == 'viernes':
    print('Ya casi termina')
elif (dia_en_teclado == 'sabado' or dia_en_teclado == 'domingo'):
    print('Sii, fin de semana')
else:
    print('El valor no es valido')