abecedario = "abcdefghijklmnñopqrstuvwxyz"

def normalizar_tilde(i):
        if i == "á":
            i = "a"
        elif i == "í":
            i = "i"
        elif i == "ó":
            i = "o"
        elif i == "é":
            i == "e"
        elif i == "ú" or "ü":
            i = "u"
        return i

def normalizar (texto):
    normalizado = ""
    for caracter in texto.lower():
        if caracter not in abecedario:
            if caracter in "áéíóúü":
                normalizado = normalizado + normalizar_tilde(caracter)
        else: normalizado = normalizado + caracter
        if caracter == " ":
            normalizado = normalizado + caracter
    return normalizado
texto = input("ingrese mensaje para normalizar")
print(normalizar(texto))
