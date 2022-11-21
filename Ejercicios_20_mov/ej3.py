def num_max_min(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print ("El mayor es", num1, "y el menor", num3) 
    elif num2 > num1 and num2 > num3:
        print ("El mayor es", num2, "y el menor", num3)
    elif num3 > num1 and num3 > num2:
        print ("El mayor es", num3, "y el menor", num2)
    else:
        print ("Son iguales")
num_max_min(19,10,32)