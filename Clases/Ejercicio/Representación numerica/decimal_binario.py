n_decimal=int(input("Introduce tu número decimal \n"))
cociente_0= False
binario= " "
while (cociente_0==False):
    binario =str(n_decimal % 2) + binario
    n_decimal= n_decimal//2
    print(n_decimal)
    if (n_decimal ==0):
        cociente_0=True

print(binario)
