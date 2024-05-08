#Escriba la función que dado un número en punto flotante retorne su parte decimal.
# Ej: si la función se llama ParteDecimal entonces ParteDecimal(4.453) devolvería el número 0.453
def parte_decimal(a):
    valor = (round (a) - a) * -1
    return  valor

resultado =parte_decimal(2.35) ### Convertir a Str con  Format F.
print(resultado)