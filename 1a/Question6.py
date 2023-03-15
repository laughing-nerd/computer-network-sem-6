n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

a=n1 if n1>n2 else n2 #Stores the bigger number
b=n1 if n1<n2 else n2 #Stores the smaller number

while(a%b!=0):
    remainder=a%b
    if (remainder!=0):
        a=b
        b=remainder
    else:
        break

print("The GCD is "+str(b))