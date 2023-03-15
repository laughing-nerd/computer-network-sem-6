import math

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

print("The sum = "+str(a+b))
print("The difference = "+str(a-b))
print("The product = "+str(a*b))
print("The dion result = "+str(a/b))
print("The floor dion result = "+str(a//b))
print("The modulus result = "+str(a%b))
print("The exponent result = "+str(a**b))
print("The floor of "+str(a)+" = "+str(math.floor(a)))
print("The floor of "+str(b)+" = "+str(math.floor(b)))

print("The ceil of "+str(a)+" = "+str(math.ceil(a)))
print("The ceil of "+str(b)+" = "+str(math.ceil(b)))