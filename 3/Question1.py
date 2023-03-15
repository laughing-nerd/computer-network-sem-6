import random

def XOR(a, b): #This function is for XOR operation without using ^ operator
    xor_output=''
    for i in range(len(a)):
        diff=abs(int(a[i])-int(b[i]))
        xor_output+=str(diff)
    return xor_output


def binary_addition(a,b): #This function is used to perform binary addition of 2 binary strings
    #Padding
    if(len(a)>len(b)):
        diff = len(a)-len(b)
        padding = "0"*diff
        b=padding+b
    elif(len(b)>len(a)):
        diff = len(b)-len(a)
        padding = "0"*diff
        a=padding+a

    n=len(a)
    sum=''
    carry=0
    for i in range(n-1, -1, -1):
        sum_int=carry+int(a[i]) + int(b[i])
        if(sum_int>1):
            carry=1
            sum_int=sum_int%2
        else:
            carry=0
        sum+=str(sum_int)
    if(carry==1):
        sum+=str(carry)
    sum=sum[::-1]
    return sum

def division(frame, generator): #Binary division using XOR
    n=len(generator)
    count=n
    a=frame[:n] #Selects a part of frame. length of the selected part is equal to the length of the generator
    while True:
        xor_output=XOR(a,generator)
        index=xor_output.find('1') #Finds the first index of 1 in the output. This is because in the next iteration, the new division will be performed on a binary number that begins with '1'
        a=xor_output[index:] #This extracts the part of the output where the first element is '1'

        #This part adds extra bit from the dividend(original frame) to the modified XOR output so as to make the binary number's length equal to the length of the generator
        if(len(a)<n):
            required=n-len(a)
            if(count+required>len(frame)): #Overflow check
                break
            else:
                a+=frame[count: count+required]
                count+=required

    if(count<len(frame)): #Adds the extra bits from the dividend to the output
        xor_output+=frame[count:]
    
    xor_output=xor_output[(len(xor_output)-(n-1)):] #This part extracts only the last n-1 bits from the output. n = length of generator
    added_result = binary_addition(frame, xor_output)
    return added_result, xor_output


frame = input("Enter the frame value: ")
generator = input("Enter the generator value: ")

print("The original frame: ", frame)
print("\n")

#--------------------- Transmitter ---------------------
n=len(generator)
#Padding
for i in range(n-1):
    frame+='0'
transmitted_frame, Remainder = division(frame, generator)
print("The transmitted frame: ",transmitted_frame)


#--------------------- Receiver ---------------------
Received = transmitted_frame

#......Noisy channel......
bit_position = random.randint(0,len(Received)-1) #Randomly selects a bit position to change
Received_Noisy= ""
for i in range(0, len(Received)): #This Changes a single random bit from a random frame
    if(i==bit_position):
        if(Received[i]=='1'):
            Received_Noisy+='0'
        else:
            Received_Noisy+='1'
    else:
        Received_Noisy+=Received[i]
print("The received frame due to Noisy channel: ", Received_Noisy)
A, Remainder = division(Received_Noisy, generator)
if(Remainder!='0'*len(Remainder)):
    print("The data was corrupted due to Noisy Channel.\n")
else:
    print("The data was not corrupted.\n")

#......Noiseless channel......
print("The received frame due to Noiseless channel: ", Received)
A, Remainder = division(Received, generator)
if(Remainder!='0'*len(Remainder)):
    print("The data was corrupted due to Noisy Channel.\n")
else:
    print("The data was not corrupted.\n")