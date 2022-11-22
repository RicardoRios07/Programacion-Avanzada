peso = float(input ("Ingrese su peso corporal en kg: "))
estatura = float(input("Ingrese su estatura en metros : "))

masa = round (peso / estatura**2,2)

print("Tu indice de masa corporal es ", masa)