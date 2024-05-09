"""
4. Como hemos visto en el curso, en Python muchas
funciones están implementadas en módulos que son archivo
s conteniendo definiciones con código fuente Python.
Para utilizar un módulo es necesario importar el módulo mediante la declaración “import” seguido del nombre del módulo.

El módulo “random” contiene la función random.randint donde random.randint(1,6) devuelve un número aleatorio entre 1 y 6 (incluidos) y que se puede utilizar para simular la tirada de un dado.

a)    Realizar un programa para simular 20 tiradas de dos dados simultáneamente, dando el promedio de la suma de los resultados de los dos dados.

b)    Realizar un programa que cuente la cantidad de veces que salió la cara 1, 2, … 6 en 30 tiradas.
"""
# A
"""import  random
i=0
dado_a = 0
dado_b = 0
while 20>=i:
    i=i+1
    dado_a = random.randint(1,6) 
    dado_b = random.randint(1,6)
    promedio= (dado_b+dado_a)/2
    print(promedio)"""
#B
import  random
i=0
dado_a = 0
cara_1=0
cara_2=0
cara_3=0
cara_4=0
cara_5=0
cara_6=0
while 30>=i:
    i=i+1
    dado_a = random.randint(1,6)
    if dado_a == 1:
        cara_1=cara_1+1
    elif dado_a ==2:
        cara_2=cara_2+1
    elif dado_a ==3 :
        cara_3= cara_3+1
    elif dado_a ==4:
        cara_4= cara_4+1
    elif dado_a == 5:
        cara_5 = cara_5+1
    else:
        cara_6  = cara_6+1
print('la cara 1:',cara_1)
print('la cara 2:',cara_2)
print('la cara 3:',cara_3)
print('la cara 4:',cara_4)
print('la cara 5:',cara_5)
print('la cara 6:',cara_6)