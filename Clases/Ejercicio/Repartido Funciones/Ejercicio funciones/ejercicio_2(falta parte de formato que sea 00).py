#Dada una hora (horas, minutos y segundos), desarrollar una función que devuelva la hora en un string en formato
# hh:mm:ss (note que podemos convertir números a strings usando la función str y podemos concatenar strings usando el operador "+").

def conversor_string(h,m,s):
    horario = str(h)+":"+str(m)+":"+str(s)
    return  horario

horario = conversor_string(1,35,6)
print(horario)