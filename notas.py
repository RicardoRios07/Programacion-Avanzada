"""
Pedir una nota al usuario
Si la nota es menor a 10 y mayor o igual a 9, imprimir Excelente.
Si la nota es menor a 9 y mayor o igual a 8, imprimir Muy bueno
Si la nota es menor a 8 y mayor o igual a 7, imprimir Bueno
Si la nota es menor a 7, imprimir reprobado
"""

nota = float (input("Ingrese una nota: "))

while nota 
    print("Ingrese una nota que no sea mayor a 10")



def clasificarNota(nota):
    
    if nota <= 10 and nota >= 9:
        print("Excelente")
    else:
        if nota < 9 and nota >= 8:
            print("Muy bueno")
        else:
            if nota < 8  and nota >= 7:
                print ("Bueno")
            else: 
                if nota < 7:
                    print("REPROBADO")

print(clasificarNota(nota))