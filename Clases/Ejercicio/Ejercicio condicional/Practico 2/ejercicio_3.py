'''
3. Escribir un programa que dibuja un rectángulo en
 pantalla utilizando el caracter “x”.
 El tamaño del rectángulo está dado por la cantidad de “x” en la base y en la altura.

Ej.: si se ingresa 7 y 5 como entrada, imprime:

xxxxxxx
x     x
x     x
x     x
xxxxxxx
'''
#altura= int(input("Introduzca la altura \n"))
#base = int(input("Introduzca la base \n"))
i=0
altura=5
base=5
intermedio= "x"+' '*(altura)+'x'
print('x'*base+'x')
while (i!=altura):
    print(intermedio)
    i=i+1
print('x'*base+'x')