#11. Escribir una función
# que realice el cálculo de
# ambas raíces reales (asumiendo que las tiene)
# de un polinomio de segundo grado y que imprima en
# pantalla ambas raíces. Los parámetros de la función
# son los coeficientes del polinomio a, b, y c. ¿Qué pasa cuando el determinante es menor que 0?

def ecuacion_cuadratica(a,b,c):
    raiz_a = (- b + (b ** 2 - 4 * a * c) ** 0.5)/(a*2)
    raiz_b = (- b - (b ** 2 - 4 * a * c) ** 0.5)/(a*2)
    return  ('La primera raíz es:',raiz_a,'la segunda raíz es',raiz_b)

test = ecuacion_cuadratica(1,5,90)
print(test)