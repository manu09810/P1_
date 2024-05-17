#7. Gematría es un sistema de origen asiro-babilonio que asigna a cada palabra o frase un valor numérico calculado sobre las letras en la palabra.
# El sistema más sencillo suma las letras en la frase dando un valor de 1 a cada “a", 2 a cada “b", 3 a cada “c”, etc. Los espacios en blanco
# y símbolos de puntuación se ignoran.
#7. Gematría es un sistema de origen asiro-babilonio que asigna a cada palabra o frase un valor numérico calculado sobre las letras en la palabra. El sistema más sencillo suma las letras en
# la frase dando un valor de 1 a cada “a", 2 a cada “b", 3 a cada “c”, etc. Los espacios en blanco y símbolos de puntuación se ignoran.

def gematria_calculadora(palabra):
    contador = 0
    abecedario = 'abcdefghijklmnñopqrstuvwxyzáíóúé'
    for i in palabra:
     posicion = abecedario.find(i)+1
    contador = contador + posicion
    return contador
test = gematria_calculadora('abc')
print(test)