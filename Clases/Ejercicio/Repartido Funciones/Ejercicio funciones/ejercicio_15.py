'''15. Escribir un programa que indique si un
número es de buena suerte o no (un número es de buena suerte si sus dígitos suman 21).
Observe que puede reutilizar inteligentemente el ejercicio anterior.'''

def ultimo_digito(n):
    i = 0
    while n % 10 != 0:
        i = i + 1
        n = n - 1
    return i
def sacar_ultimo_dig(n):
     return (n - ultimo_digito(n)) // 10

def reductor_cifras(n):
    num = n
    acumulador = 0
    while num >= 1:
        acumulador = acumulador + ultimo_digito(num)
        num = sacar_ultimo_dig(num)
    print('-----------------------------')
    if acumulador == 21:
        return 'Se trata de un numero de la buena suerte'
    else:
        return 'No se trata de un numero de la buena suerte'



n = int(input('Introduce tu numero\n'))
print(reductor_cifras(n))

