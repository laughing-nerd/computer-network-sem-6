def calculate(a,b,op):
    if(op.lower()=='add'):
        print("The sum is ",(a+b))
    elif(op.lower()=='sub'):
        print("The difference is ",(a-b))
    elif(op.lower()=='prod'):
        print("The product is ",(a*b))
    elif(op.lower()=='div'):
        print("The divison is ",(a/b))
    elif(op.lower()=='exp'):
        print("The exponent is ",(a**b))
    elif(op.lower()=='mod'):
        print("The modulus is ",(a%b))
    else:
        print("Invalid operation")

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

choice=input("\nadd - Addition\nsub - Subtraction\nprod - Product\ndiv - Division\nexp - Exponential\nmod - Modulus\nEnter your choice: ")
calculate(a,b,choice)
