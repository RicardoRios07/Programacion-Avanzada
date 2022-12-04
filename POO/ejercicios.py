import math
class Punto:
    def __init__(self, X = 0, Y = 0):
 
        self.X = X
        self.Y = Y
 
    def __str__(self):
        return f"({self.X}, {self.Y})"
 
    def cuadrante(self):
        cadena ="{} pertenece al {} cuadrante"
        if self.X > 0 and self.Y > 0:
            print(cadena.format(self,'primer'))
        elif self.X < 0 and self.Y > 0:
            print(cadena.format(self,'segundo'))
        elif self.X < 0 and self.Y < 0:
            print(cadena.format(self,'tercer'))
        elif self.X > 0 and self.Y < 0:
            print(cadena.format(self,'cuarto'))
        elif self.X != 0 and self.Y == 0:
            print(f"{self} se sitúa sobre el eje X")
        elif self.X == 0 and self.Y != 0:
            print(f"{self} se sitúa sobre el eje Y")
        else:
            print(f"{self} se encuentra sobre el origen")
 
    def vector(self, p):
        return f"El vector entre {self} y {p} es ({p.X - self.X}, {p.Y-self.Y})"
 
    def distancia(self, p):
        d = math.sqrt ( (p.X - self.X)**2 + (p.Y - self.Y)**2 )
        return f"La distancia entre los puntos {self} y {p} es {d}"
 
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)
 
A.cuadrante()
C.cuadrante()
 
print(A.vector(B))
print(B.vector(A))
 
 
 
print(A.distancia(B))
print(B.distancia(A))


class Rectangulo:
    
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
 
    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )
 
    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ) )
 
    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ) )
 
class Rectangulo:
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
 
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura
 
    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )
 
    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ) )
 
    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ) )
 
 
 
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)
 
A.cuadrante()
C.cuadrante()
D.cuadrante()
 
A.vector(B)
B.vector(A)
 
 
 
A.distancia(B)
B.distancia(A)
 
A.distancia(D)
B.distancia(D)
C.distancia(D)
 
R = Rectangulo(A, B)
R.base()
R.altura()
R.area()