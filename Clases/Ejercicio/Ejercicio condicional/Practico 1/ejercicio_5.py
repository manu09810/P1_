"""5. Escribir un programa que, dados dos números que se leen por teclado imprime "Verdadero"
 si el resultado de multiplicar ambos números es 1 y "Falso" si no lo son. Ej.: 2 y 0.5, 5 y 0.2, 2.5 y 0.4."""
numero_a= float(input("Introduzca el primer numero:\n"))
numero_b= float(input("Introduzca el segundo numero:\n"))
if(numero_a*numero_b==1):
    print("Verdadero")
else:
    print("Falso")