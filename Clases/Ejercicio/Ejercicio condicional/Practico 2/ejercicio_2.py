"""
2. Leer números enteros positivos de teclado,
hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado."""

n = ''
n_max=0
while n!=0:
    n = int(input())
    if n>0 and n>n_max:
        n_max=n
print(n_max)