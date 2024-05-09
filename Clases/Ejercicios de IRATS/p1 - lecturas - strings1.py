"""Escribe una función en main.py que recibe como
 parámetro un string y devuelva el string dado vuelta. El desafío es hacerlo con un while accediendo
a los elementos del string por su índice desde la última posición a la primera.
Solo debes escribir la función (si quieres puedes probarla
desde la consola). Una vez que la tengas terminada debes hacer el test de unidad.
Si tienes dificultades en realizarlo, hemos incluido
 un archivo con la solución (pero solo mirar luego de haber hecho el esfuerzo de resolverlo)."""


#Si meto abcd que devuelva dcba
def dar_vuelta_str(string_a):
    digitos= len(string_a)-1
    resultado= ""
    i = digitos
    while (i >= 0):
        resultado = resultado +string_a[i]
        i = i-1
    return resultado

print(dar_vuelta_str("Lo70969s"))

