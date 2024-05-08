#Dadas 2 horas (horas, minutos y segundos) desarrollar una funció
# n para averiguar la diferencia en segundos de las 2 horas.
def segundos_por_hora(h,m,s):
    segundos= (h*60**2)+(m*60)+s
    return  segundos
def diferencia_horas(a,b):
    if a>=b:
        valor= a-b
    else:
        valor= b-a
    return  valor

test = diferencia_horas(segundos_por_hora(1,0,0),segundos_por_hora(0,0,0))
print(test)