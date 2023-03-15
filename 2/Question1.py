STUFF=5 #This specifies after how many bits the data will be stuffed with 0
Stuff_Position=[] #This will store the the position of stuffed bits

def bit_stuff(data):
    global Stuff_Position
    stuffed_output=""
    count=0
    for i in range(len(data)):
        if (count==STUFF):
            stuffed_output+='0'
            Stuff_Position.append(len(stuffed_output)-1)
            count=0
        if(data[i]=='1'):
            count+=1
        else:
            count=0
        stuffed_output+=data[i]
    return stuffed_output

def bit_destuff(data):
    destuffed_output=""
    for i in range(len(data)):
        if(i not in Stuff_Position):
            destuffed_output+=data[i]
    return destuffed_output

n=int(input("Enter the number of bits: "))
data=""
for i in range(n):
    data+=input(f"Enter the bit for position {i}: ")
stuff=bit_stuff(data)
print("Original data: ",data)
print("Bit stuffed output: ", stuff)
print("Position of stuffed bits: ", Stuff_Position)
print("Bit de-stuffed output: ", bit_destuff(stuff))