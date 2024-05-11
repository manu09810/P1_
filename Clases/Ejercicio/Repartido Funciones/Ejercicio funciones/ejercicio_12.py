#12. Escribir una función que, dado una año
# permita determinar si el mismo es bisiesto
# devolviendo True o False en caso contrario.
# Para esta función solo se utilizará una expresión lógica.
def bisiesto_o_no(n):
    estado = False
    if(n % 4 == 0 or (n % 100 == 0 and n % 400 != 0)):
        estado = True
    return estado