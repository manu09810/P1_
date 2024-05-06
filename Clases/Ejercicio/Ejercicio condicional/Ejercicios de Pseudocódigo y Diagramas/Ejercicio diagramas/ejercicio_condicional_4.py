"""4) Elaborar un algoritmo (diagrama de flujo) que solicite el número de respuestas
correctas, incorrectas y en blanco que ha tenido un estudiante en un examen. Luego
el algoritmo deberá mostrar el puntaje obtenido, siendo que cada respuesta correcta
tendrá 4 puntos, cada respuesta incorrecta tendrá -1 y las respuestas en blanco
valen 0"""

respuestas_correcta= int(input("¿Cuántas respuestas correctas tiene el alumno? "))
respuestas_incorrecta= int(input("¿Cuántas respuestas tiene incorrectas el alumno? "))
respuestas_blanca= int(input("¿Cuántas respuestas en blanco tiene el alumno? "))

puntaje= (4*respuestas_correcta+respuestas_incorrecta*-1+respuestas_blanca*0)
print()
print("El puntaje es:",puntaje)
print()