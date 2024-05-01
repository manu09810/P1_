"""5) Encontrar las raíces de un polinomio de segundo grado mediante un algoritmo
expresado en pseudocódigo. El programa debe indicar si no tiene raíces reales, si
tiene raíces dobles (y su valores) o si tiene dos raíces reales (y su valores)"""
from math import  sqrt
a=int(input('Ingrese el primer coeficiente:\n'))
b=int(input('Ingrese el segundo coeficiente:\n'))
c=int(input('Ingrese el tercer coeficiente:\n'))

determinante = b**2 - 4*a*c
if determinante < 0:
    raiz_a = ' imaginaria'
    raiz_b = 'imaginaria'
else:
    if determinante == 0:
        raiz_a = (-b+ sqrt(determinante)) / 2*a
        raiz_b = raiz_a
    if determinante > 0:
        raiz_a = (-b + sqrt(determinante)) / 2 * a
        raiz_b = (-b - sqrt(determinante)) / 2 * a
print()
print('La primera raiz es',raiz_a,'\n')
print('La segunda raiz es',raiz_b,'\n')