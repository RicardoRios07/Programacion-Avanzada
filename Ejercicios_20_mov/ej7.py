def mayor_menor_edad (lista):
    for i in lista:
        if i > 18:
            print ("Es mayor de edad")
        else:
            print ("Es menor de edad")
mayor_menor_edad([15,24,19,17,4,8,2,90,2,19])