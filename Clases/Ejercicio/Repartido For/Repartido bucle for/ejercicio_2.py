'''2. Para utilizar un módulo es necesario
importar el módulo mediante la declaración
“import” seguido del nombre del módulo.
Utilizaremos el ya conocido módulo “random” y su
función random.randint donde random.randin
t(1,6) devuelve un número aleatorio entre 1 y 6 (incluidos).'''

#a. Realizar un programa para simular 20 tiradas de dos dados simultáneamente, dando el promedio
# de la suma de los resultados de los dos dados. Esta vez resolver el ejercicio con la estructura
# de repetición for.

#b. Realizar un programa que cuente la cantidad de veces que salió la cara 1, 2, … 6 en 30 tiradas.
# Esta vez resolver el ejercicio con la estructura de         repetición for.

import  random

#a)
'''n = 20
acumulador = 0
for i in range(n):
    dado_a = random.randint(1, 6)
    dado_b = random.randint(1, 6)
    promedio = round((dado_a+dado_a) / 2)
    acumulador = acumulador + dado_a + dado_b
    promedio_total = acumulador / n
    print(promedio)
print('El promedio total:',promedio_total)
'''
#b
n = 30
acumulador = 0
nums_posible ='12356'

for i in range(n):
    dado_a = random.randint(1, 6)
    dado_b = random.randint(1, 6)
    print(i)