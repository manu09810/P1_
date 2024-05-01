"""6) Para calcular el sueldo de un empleado, el requisito básico es conocer la cantidad
de horas trabajadas en el mes y el valor por hora que se paga. Hacer un algoritmo
en diagrama de flujo que pida estos datos. Luego, en el caso de que el número de
horas trabajadas sea mayor a 40, esas horas adicionales (las que superan las 40)
deben pagarse al doble de su valor por hora. Ejemplo: si un empleado cobra
10$xhora y trabaja 30 horas, su sueldo se calculará como 300$. En cambio, si
trabajara 50 horas, cobrará 40x10$ las primeras 40 horas + 10x20$ las horas extras."""

horas_trabajadas= int(input("Cantidad de horas trabajadas:  "))
sueldo_hora= int(input(("Cantidad de sueldo:  ")))

sueldo_neto= horas_trabajadas*sueldo_hora
sueldo_horas_adicionales= (horas_trabajadas-40)*sueldo_hora
if horas_trabajadas>40:
   print(sueldo_horas_adicionales+sueldo_neto)
else:
    print(sueldo_neto)