cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interés porcentual anual: "))
años = int(input("Años: "))

print("El capital  final es : " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))