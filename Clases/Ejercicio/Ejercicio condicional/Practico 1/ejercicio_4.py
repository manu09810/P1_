"""4. Escriba un programa que lea tres números
 (n, linf, lsup). Esta función debería imprimir "verdadero" o "falso" si linf <= n <= lsup
 (es decir, si n está entre linf y lsup)."""

n= int(input("Introduzca el valor n:\n"))
linf= int(input("Introduzca el valor linf :\n"))
lsup= int(input("Introduzca el valor lsup :\n"))
print(n,"es n")
print(linf,"es linf")
print(lsup,"es lsup")
if (linf <=n and n<=lsup):
    print("verdadero")
else:
    print("falso")