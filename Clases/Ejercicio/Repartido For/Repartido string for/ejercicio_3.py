#3. Escribir una función que reciba una cadena de caracteres
# y retorne una nueva cadena con los caracteres espacio (“ “)
# reemplazados por el carácter “;”.

def quita_espacios(n):
    resultado = ''
    for i in n:
        if i in ' ':
            i =';'
        resultado= resultado+i
    return resultado
print(quita_espacios('2142068w59e b5 35 w w 2 2'))