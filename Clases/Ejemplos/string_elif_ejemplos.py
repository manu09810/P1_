#nombre=input("Nombre")
#edad=input("Edad")
peso=input("Peso(Kg)")
altura=input("Altura(mts)")
imc= float(peso)/float(altura)**2 ## Aqui existia un error, se intento dividir una str en python, eso esta mal.
print()
#print("Nombre:",nombre)
#print("Edad:",edad)
print("Peso:",peso)
print("Altura:",altura)
print("IMC:",imc)
"""if imc<17.5:
    print("Bajo peso") # Version Else 
else:
        if(imc<24.9):
            print("Peso adecuado")
        else:
            if(imc<29.9):
                print("Sobre peso")
            else:
                print("Obesidad")"""

if imc<17.5: # usando elif, metodo más organiado
    print("Bajo peso")
elif(imc<24.9):
    Aprint("Peso adecuado")
elif(imc<29.9):
    print("Sobre peso")
else:
    print("Obesidad")
print()
