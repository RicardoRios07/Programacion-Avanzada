"""
Crear un script que indique si el usuario es mayor de edad, 
menor de edad o es parte de la tercera edad.

"""

edad = int(input("Ingrese du edad: "))

if (edad < 17):
    print("Usted es menor de edad")
else: 
    if(edad <= 49 ):
        print("Usted es mayor de edad")
    else: 
        if(edad <= 120):
            print("Usted pertenece a la tercera edad")
        else:
            if(edad > 120):
                print("No existe en este rango")
