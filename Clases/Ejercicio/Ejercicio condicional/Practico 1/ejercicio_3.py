"""3. Escriba un programa que pida los datos de peso y altura de un adulto y muestre
por pantalla la categoría que corresponde al índice de masa corporal
 (tenga en cuenta que para calcular este índica puede utilizar la funcionalidad desarrollada en el práctico anterior)."""
peso= float(input("Ingrese su peso\n"))
altura= float(input("Ingrese la altura en metros\n"))

imc= peso/altura**2
print("El IMC es: \n",imc)