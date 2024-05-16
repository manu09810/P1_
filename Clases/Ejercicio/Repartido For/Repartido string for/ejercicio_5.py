# 5. Crear una función “pangrama” que recibe
# una cadena de caracteres e indica si la misma es un pangrama. Un pangrama es una cadena de caracteres que contiene todas las letras posibles de alfabeto
# ya sea en mayúsculas o minúsculas (español para nuestro caso).
def detectar_panagrama(palabra):
    bandera = False
    abecedario = 'qwertyuiopasdfghjklzxcvbnmñáéíóúü'
    for i in palabra.lower():
        if not i  == palabra.lower():
            bandera = True

test = detectar_panagrama("El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña toca el saxofón detrás del palenque de paja")
print(test)