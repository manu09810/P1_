"""


14. Leer un número entero positivo (mayor que 0) desde teclado e imprimir la suma de los dígitos que lo componen.
Tenga en cuenta que para esto vamos a utilizar las siguientes funciones (que deberá implementar):

- ultimodigito( n ): dado un número n (por ejemplo 456), deberá retornar el último de los dígitos (ej: 6)

- sacarultimodigito( n ): dado un número n (ej: 456) deberá retornar el mismo número pero sin su último dígito (ejL 45)

Con estas dos funciones componga el programa solicitado. Tenga en cuenta que dado un número podemos sumar sus dígitos
identificando uno por uno de derecha a izquierda. Por ejemplo, para el número 1456 podemos obtener ultimodigito
(es decir, identificamos el 6) y luego achicar el número con sacarultimodigito (quedaría 145).
Si repetimos este procedimiento identificaremos todos los dígitos y el número se irá reduciendo hasta 0.


"""
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
    print('El valor sumado de los digitos del  n:',n,'es:')
    return acumulador



n = int(input('Introduce tu numero\n'))
print(reductor_cifras(n))

