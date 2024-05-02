n_decimal=int(input("Introduce tu número decimal \n"))
binario= " "
while (n_decimal>0 ):
    binario =str(n_decimal % 2) + binario
    n_decimal= n_decimal//2
    print(n_decimal)
print(binario)
