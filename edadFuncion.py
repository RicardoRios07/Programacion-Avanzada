"""
Crear una funcion que permita conocer el rango de edad de  una persona

"""



nombre = input("Ingrese su nombre: ")
edad = int(input("Edad: "))



def edadCalcular(edad):
    if edad <= 18:
        print (nombre, "Es mayor de edad")
    else:
        print(nombre, "Es menor de edad")

edadCalcular(edad)