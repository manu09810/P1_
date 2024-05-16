#4. Escribir una función que recibe una
# cadena de caracteres como parámetros con
# una fecha de la forma “dd/mm/aaaa” y
# devuelve la fecha en formato “aaaa‐ mm-dd”.

#Ej.: 10/11/1977 ->1977‐11‐10

def formatear_estilo_amd(cadena):
    return cadena[6:] + '-' + cadena[3:5] + '-' + cadena[0:2]

test = formatear_estilo_amd("10/11/1977")
print(test)