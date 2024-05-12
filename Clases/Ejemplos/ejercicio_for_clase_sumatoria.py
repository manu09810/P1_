#Power point de sumatorias 
'''
n = int(input())+1
sumatoria=0
for i in range(1,n):
    sumatoria = sumatoria+i**3
print(sumatoria)
'''
'''n = int(input())+1
sumatoria=0
for j in range(1,n):
    print(j)
    sumatoria = sumatoria+j+2
print(sumatoria)'''

'''n = int(input())+1
sumatoria=0
for i in range(2,n):
        print(i)
        sumatoria = sumatoria+(i**2)/((i-1)*(i+1))
print(sumatoria)'''

### Se puede crear una funcion a partir de esot para facilar el proceso
palabra= 'bacalao'
contador = 0
for i in range(len(palabra)):
    letra= palabra[i].lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == '':
        contador=contador+1
print('La palabra tiene',contador,'vocales')


## Solucion propia
for i in range(len(palabra)):
    letra= palabra[i].lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == '':
        contador=contador+1
print('La palabra tiene',contador,'vocales')
vocales='aeiou'
for i in range(len(palabra)):
    letra= palabra[i].lower()
    if letra in vocales:
        contador=contador+1
