#Dado el peso y altura de un adulto, desarrollar una función que devuelva un string donde se indique
# la categoría del índice de masa corporal.
def categortizador_imc(peso, altura):
    imc = peso/altura**2
    print(imc)
    if(imc<18.5):
        categoria = "Peso insuficiente"
    elif(imc > 18.5 and 24.9> imc):
        categoria = "Peso normal"
    elif (imc > 25.0 and 29.9 > imc):
        categoria = "Peso sobrepeso"
    else:
        categoria = "Peso obesidad"
    return categoria

resultado= categortizador_imc(90,1.9)

print(resultado)