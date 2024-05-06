"""6. Escriba un programa que lea el candidato por el cual el usuario va a votar.
 Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
 Según el candidato elegido (A, B ó C, en forma de string) se imprimirá el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”.
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”."""



partido_votado= input("Eilja su partido:"+"\nA) Partido A"+"\nB) Partido B"+"\nC) Partido C"+"\n")
if(partido_votado=="A" or partido_votado=="B" or  partido_votado =="C"):
    print("El partido votado es",partido_votado)
else:
    print("Opción errónea")