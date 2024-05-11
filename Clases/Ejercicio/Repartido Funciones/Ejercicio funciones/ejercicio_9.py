#9.
# Escribir una función que tenga como parámetro un
# número y que devuelva cuantas cifras tiene ese número.
def contar_cifras(n):
    i=0
    while n>0:
        i=i+1
        n= n//10
    return i

test = contar_cifras(200031)
print(test)