binary1=[]
binary2=[]

def bitwise(a,b,n):
    output_dict={
        'AND':[],
        'OR':[],
        'XOR':[]
    }
    for i in range(n):
        output_dict.get('AND').append(a[i]&b[i])
        output_dict.get('OR').append(a[i]|b[i])
        output_dict.get('XOR').append(a[i]^b[i])

    
    print(f"The AND bitwise result is: {output_dict['AND']}\nThe OR bitwise result is: {output_dict['OR']}\nThe XOR bitwise result is: {output_dict['XOR']}")


n=int(input("Enter the number of bits: "))
#Binary number 1
for i in range(n):
    n1=int(input(f"Enter the bit for position {i} for the first binary number: "))
    binary1.append(n1)

#Binary number 2
for i in range(n):
    n2=int(input(f"Enter the bit for position {i} for the second binary number: "))
    binary2.append(n2)

print("The first binary number: ",binary1)
print("The second binary number: ",binary2)

bitwise(binary1, binary2, n)



