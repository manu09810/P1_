"""
Mejora tu lógica de programación.

Utiliza el lenguaje de programación que tú quieras para resolver ejercicios que te ayudarán a mejorar tu forma de pensar y enfrentarte a retos de código.

Consulta correcciones de la comunidad en los repositorios de código de los diferentes retos. Se han dividido entre los resueltos en 2022 y 2023 (consulta su etiqueta).

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""
n=1
while (n<=100):
    if (n%5==0 and n%3 == 0):
        print('fizzbuzz')
    elif(n%5==0):
        print('buzz')
    elif(n%3==0):
        print('fizz')
    else:
        print(n)
    n=n+1
