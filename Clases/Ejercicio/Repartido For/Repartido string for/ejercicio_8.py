#8. Las palabras mágicas son aquellas que su valor gemátrico es 21.
# Crear una función que devuelva True si una palabra es mágica y False en caso contrario.
def gematria_calculadora(palabra):
    contador = 0
    abecedario = 'abcdefghijklmnñopqrstuvwxyzáíóúé'
    for i in palabra:
        posicion = abecedario.find(i)+1
        contador = contador + posicion
    if contador == 21:
        return  True
    else: return False
test = gematria_calculadora('ccccccba')
print(test)