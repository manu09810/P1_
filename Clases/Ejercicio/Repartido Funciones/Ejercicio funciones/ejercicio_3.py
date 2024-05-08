"""Escriba la función “formateanombre” que reciba como parámetros de entrada el nombre, el apellido (strings) y el número de cédula (número entero) y devuelva un string con la siguiente frase:
apellido, nombre tiene el número de cédula número"""

def formateanombre(nombre,apellido,n_cedula):
        resultado = nombre + " " +apellido + " "+ str(n_cedula)
        return resultado

valor =formateanombre("Manuel","Lorenzo",555661601)
print(valor)