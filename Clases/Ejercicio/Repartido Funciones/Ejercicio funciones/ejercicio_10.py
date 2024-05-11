# 10. Escribir una función que dados 3 números, devuelva cuál es el mayor.
def max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

test = max(3,3,1)
print(test)