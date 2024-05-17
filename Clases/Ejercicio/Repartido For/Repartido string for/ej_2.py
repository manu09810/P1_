#2. Realice lo mismo que en el ejercicio anterior,
# \pero que escriba las letras del string en orden
# inverso (también una letra por línea).
# ¿Puede implementar las dos versiones propuestas?

string_ingresar = input('Ingrese el valor')

for i in range(len(string_ingresar)):
    print(string_ingresar[-i])