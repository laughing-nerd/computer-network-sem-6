l1=[]
l2=[]
newList=[]

for i in range(10):
    n=int(input("Enter the number for list 1: "))
    l1.append(n)

for i in range(5):
    n=int(input("Enter the number for list 2: "))
    l2.append(n)

print("List 1: ", end="")
print(l1)
print("List 2: ", end="")
print(l2)

while(len(l1)>0 and len(l2)>0):
    if(l1[0]<l2[0]):
        newList.append(l1[0])
        l1.pop(0)
    elif(l2[0]<=l1[0]):
        newList.append(l2[0])
        l2.pop(0)

#This sorting part ensures that the left over list, when added with newList[], is a properly sorted one
listToSort = l1 if(len(l1)>0) else l2

for i in range(0,len(listToSort)-1):
    for j in range(0,len(listToSort)-i-1):
        if(listToSort[j]>listToSort[j+1]):
            temp=listToSort[j]
            listToSort[j]=listToSort[j+1]
            listToSort[j+1]=temp

newList.extend(listToSort)
print("After merging the new list is: ",end="")
print(newList)