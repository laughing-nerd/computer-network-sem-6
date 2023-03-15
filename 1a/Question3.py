l=[]

for i in range(10):
    n=int(input("Enter a number: "))
    l.append(n)

print("Your list : ", end="")
print(l)

#Bubble sort 
for i in range(0,len(l)-1):
    for j in range(0,len(l)-i-1):
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp

print("The list after sorting in Ascending Order: ", end="")
print(l)
print("The list after sorting in Descending Order: ", end="")
print(l[::-1])