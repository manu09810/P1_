"""
cadena = "abcdef"
j = 0
resultado = ""
for i in cadena:
    j = j - 1
    resultado = resultado + cadena[j]
print(resultado)"""
### Solución del probelma para el caso de invertir palabra
"""
def reversa(cadena):
    nueva_cadena = ""
    for letra in cadena:
        nueva_cadena = letra + nueva_cadena ### Cambio a diferencia de mi programa  realiza la concatenación en el orden al reves
        return  nueva_cadena
"""
###
"""
vocales = "aeiou"
palabra = input()
resultado = ""
for i in palabra:
    letra = i.lower()
    if letra in vocales:
        if letra == "a" or letra == "á":
            i = 1
        elif letra == "e" or letra == "é":
            i = 2
        elif letra == "i" or letra == "í":
            i = 3
        elif letra == "o" or letra == "ó":
            i = 4
        elif letra == "u" or letra == "ú":
            i = 5
    resultado = resultado + str(i)
print(resultado)
"""

### Solución del profesor
# Parto de una estrctura vacía
"""
def cambia_vocal(cadena):
    nueva_cadena = " "
    for letra in cadena:
        if letra in "aeiouAEIOU":
            nueva_cadena = nueva_cadena + "1"
        else:
            nueva_cadena = nueva_cadena + letra
    return  nueva_cadena
a = cambia_vocal("")
print(a)"""

## Nueva solución con range
palabra = input().lower()
vocal = "aeiou"
resultado = ""
for i in range(len(palabra)):
    if palabra[i] in vocal[0]:
        i = 1
    elif palabra[i] in vocal[1]:
        i = 2
    elif palabra[i] in vocal[2]:
        i = 3
    elif palabra[i] in vocal[3]:
        i = 4
    elif palabra[i] in vocal[4]:
        i = 5
    resultado = resultado + str(i)
print(resultado)