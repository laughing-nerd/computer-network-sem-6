import random

CHECKSUM_BIT = 8 #This defines the number of bits in every frame
def binary_addition(a,b):
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

DATA = input("Enter the data: ") #32 bit data
if(len(DATA)<32): #Zero Padding if the data is not of 32 bit length
    diff=32-len(DATA)
    DATA+='0'*diff

#--------------------- Transmitter ---------------------

#Frame creation
frame_dict={}
last_pos=-1
for i in range(len(DATA)):
    pos=i//CHECKSUM_BIT
    if(pos!=last_pos):
        frame_dict.update({ f"frame{pos}": "" })
        last_pos=pos
    frame_dict[f"frame{pos}"]+=DATA[i]

#This is used to find the sum of all the frames
val='0'
sum=''
for i in range(0,4): #Assuming that the input is of 32 bits and each frame is of 8 bit length
    number = frame_dict[f"frame{i}"]
    sum=binary_addition(val, number)
    val=sum

#This is used to find the 1's complement of the sum obtained
newSum=''
for i in range(0,len(sum)):
    if(sum[i] == '1'):
        newSum+='0'
    else:
        newSum+='1'
frame_dict.update({"frame4":newSum})
print("Transmitted frame: ", frame_dict)
print("\n")

#--------------------- Receiver ---------------------

#......Noisy channel......
Received_Noisy = frame_dict.copy()
frame_number = random.randint(0,4) #Randomly selects a frame to change
bit_position = random.randint(0,7) #Randomly selects a bit position to change
affected_frame = Received_Noisy[f"frame{frame_number}"]
newFrameContent = ""
for i in range(0, len(affected_frame)): #This Changes a single random bit from a random frame
    if(i==bit_position):
        if(affected_frame[i]=='1'):
            newFrameContent+='0'
        else:
            newFrameContent+='1'
    else:
        newFrameContent+=affected_frame[i]
Received_Noisy[f"frame{frame_number}"] = newFrameContent #The transmitted frame is modified due to noisy channel

#Find the sum of the Received frames
print("Received data in Noisy channel", Received_Noisy)
val='0'
sum=''
for i in range(0,5): 
    number = Received_Noisy[f"frame{i}"]
    sum=binary_addition(val, number)
    val=sum
if(sum!='1'*8):
    print("The data was corrupted due to Noisy channel.\n")
else:
    print("The data is not corrupted.\n")


#......Noiseless channel......
Received_Noiseless = frame_dict.copy()

#Find the sum of the Received frames
print("Received data in Noiseless channel", Received_Noiseless)
val='0'
sum=''
for i in range(0,5): 
    number = Received_Noiseless[f"frame{i}"]
    sum=binary_addition(val, number)
    val=sum
if(sum!='1'*8):
    print("The data was corrupted due to Noisy channel.\n")
else:
    print("The data is not corrupted.\n")