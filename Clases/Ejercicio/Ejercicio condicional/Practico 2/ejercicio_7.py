'''7. Escribir un programa que indique si
un número es de buena suerte o no (un número
 es de buena suerte si sus dígitos suman 21).
Observe que puede reutilizar inteligentemente el ejercicio anterior.'''
def ultimo_digito(n):
    i = 0
    while n % 10 != 0:
        n= n - 1
        i= i + 1
    return i

def sacar_ultimo_digito(n):
   return (n-ultimo_digito(n))// 10

n = int(input(''))
suma_total = 0
while n>0:
     suma_total= suma_total+ultimo_digito(n)
     n= sacar_ultimo_digito(n)

if suma_total == 21:
    print("es un numero de buena suerte")