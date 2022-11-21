def saludoConParametros(nombre):
    return "Hello", nombre
saludar = saludoConParametros("Rick")
print(saludar)



#FUNCIONES SIN PARAMETROS

def sumaSinParametros():
    return 7+4

print(sumaSinParametros())


def sumaSinParametros(num1,num2):
    return num1 + num2 

print( sumaSinParametros(4,5))


def restaSinParametros(num1,num2):
    return num1 - num2

print(restaSinParametros(9,3))
