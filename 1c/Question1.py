import math
n = int(input("Enter the total number of bits: "))
frames = int(input("Enter the total number of frames: "))
bits_per_frame = math.ceil(n/float(frames))
frame_dict={"frame1":[]}

frameCount=1
paddingCounter=1
print(f"Enter the bits for frame {frameCount}...")
while(frameCount<=frames):
    if(paddingCounter<=n):
        bit=int(input("Enter the bit: "))
        frame_dict[f"frame{frameCount}"].append(bit)
    else:
        frame_dict[f"frame{frameCount}"].append(0)
    
    if(paddingCounter%bits_per_frame==0):
        frameCount=frameCount+1
        if(frameCount<=frames):
            frame_dict.update({f"frame{frameCount}":[]});
            print(f"Enter the bits for frame {frameCount}...")
    paddingCounter=paddingCounter+1

#Performing XOR on only the first 2 frames
XOR=[]
for i in range(bits_per_frame):
    XOR.append(frame_dict["frame1"][i]^frame_dict["frame2"][i])

#Printing everything
count=1
for i in frame_dict.values():
    print(f"Frame {count}: ", end="")
    print(i)
    count=count+1
print("The XOR of Frame 1 and Frame 2 is: ", end="")
print(XOR)
