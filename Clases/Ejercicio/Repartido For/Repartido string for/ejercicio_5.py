# 5. Crear una función “pangrama” que recibe
# una cadena de caracteres e indica si la misma es un pangrama. Un pangrama es una cadena de caracteres que contiene todas las letras posibles de alfabeto
# ya sea en mayúsculas o minúsculas (español para nuestro caso).


"""
def detector_panagrama(palabra):
    abecedario = ('abcdefghijklmnñopqrstuvwxyz')
    resultado = "true"
    palabra_normalizada = palabra.strip().lower()
    for i in abecedario:
        i
        if i not in palabra_normalizada:
            resultado = "false"
    return resultado
test = detector_panagrama('el viejo señor gomez pedia queso kiwi y habas pero le ha tocado un saxofon')
print(test)"""

def detector_panagrama(palabra):
    abecedario = ('abcdefghijklmnñopqrstuvwxyz')
    resultado = "true"
    palabra_normalizada = palabra.strip().lower()
    for i in abecedario:
        if i == "a" or i == "i" or i == "o" or i == "u" or i == "e":

        if i not in palabra_normalizada:
            resultado = "false"
    return resultado
test = detector_panagrama('el viejo señor gomez pedia queso kiwi y habas pero le ha tocado un saxofon')
print(test)