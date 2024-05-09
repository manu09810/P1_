#Ejercicio para comprobar hablidad con for.
def contar_letras(cadena, letra):
  j=0
  for i in cadena:
    if i == letra:
      j=j+1
  return j
print(contar_letras('papa','6'))