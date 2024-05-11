'''6. Leer un número entero positivo (mayor que 0) desde teclado e imprimir la suma de los dígitos que lo componen. Tenga en cuenta que para esto vamos a utilizar las siguientes funciones (que deberá implementar):
- ultimodigito( n ): dado un número n (por ejemplo 456), deberá retornar el último de los dígitos (ej: 6)
- sacarultimodigito( n ): dado un número n (ej: 456) deberá retornar el mismo número pero sin su último dígito (ejL 45)
Con estas dos funciones componga el programa solicitado. Tenga en cuenta que dado un número podemos sumar sus dígitos identificando uno por uno de derecha a izquierda. Por ejemplo, para el número 1456 podemos obtener ultimodigito (es decir, identificamos el 6) y luego achicar el número con sacarultimodigito (quedaría 145). Si repetimos este procedimiento identificaremos todos los dígitos y el número se irá reduciendo hasta 0.
'''
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
     print(n)
print(suma_total)