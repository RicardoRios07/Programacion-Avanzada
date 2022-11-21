def num_min(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        print ("El menor es: ", num1) 
    elif num2 < num1 and num2 < num3:
        print ("El menor es: ", num2)
    elif num3 < num1 and num3 < num2:
        print ("El menor es: ", num3)
    else:
        print ("Son iguales")
num_min(19,10,32)