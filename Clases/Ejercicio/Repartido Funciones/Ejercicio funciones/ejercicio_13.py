"""
EJERCICIOS ADICIONALES


13. Recordemos el algoritmo de Hailstone realizado semanas atrás. El número de Hailstone corresponde al número de transformaciones sucesivas que se deben aplicar a un número entero hasta sea transformado en 1.

Las dos reglas de transformación son:

  a)  Si n es impar, multiplicar por 3 y sumar 1 para crear el nuevo valor de n.

  b)  Si n es par, dividir entre 2.

Por ejemplo, si n = 7, se hacen las transformaciones siguientes:

7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Definir una función en python que dado un número retorne el número de Hailstone (transformaciones).


"""
def hailstone(n):
    i = 0
    while n > 1:
        i =  i + 1
        if n % 2 == 0:
            n = round(n / 2)
        else:
            n = n * 3 + 1
    return  i
test = hailstone(200)
print(test)
