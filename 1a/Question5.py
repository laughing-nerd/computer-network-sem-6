n=int(input("Enter the length of the list: "))
l=[]

for i in range(n):
    inputNumnber=int(input("Enter the number: "))
    l.append(inputNumnber)

print("The original list: ", end="")
print(l)

#Selection sort
for i in range(0, n-1):
    for j in range(i+1, n):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("List after using Selection sort: ", end="")
print(l, end="\n")

#Quick Sort

def swap(a, b, arr):
    if(a!=b):
        temp=arr[a]
        arr[a]=arr[b]
        arr[b]=temp

def partition(l, start, end):
    pivot_index=start
    pivot=l[pivot_index]

    while (start<end):
        while(start<len(l) and l[start]<=pivot):
            start=start+1
        while(l[end]>pivot):
            end=end-1
        if(start<end):
            swap(start, end, l)
    swap(pivot_index, end, l)
    return end

def quick_sort(l, start, end):
    if (start<end):
        pi=partition(l,start,end)
        quick_sort(l, start, pi-1)
        quick_sort(l, pi+1, end)

quick_sort(l, 0, n-1)
print("List after using Quick Sort: ", end="")
print(l, end="\n")

#Merge Sort
def merge(arr1, arr2):
    newArr=[]
    while(len(arr1)>0 and len(arr2)>0):
        if(arr1[0]<arr2[0]):
            newArr.append(arr1[0])
            arr1.pop(0)
        elif(arr2[0]<=arr1[0]):
            newArr.append(arr2[0])
            arr2.pop(0)

    remaining_list = arr1 if(len(arr1)>0) else arr2
    newArr.extend(remaining_list)
    return newArr

def merge_sort(arr):
    if(len(arr)<=1):
        return
    mid=len(arr)//2
    merge_sort(arr[:mid])
    merge_sort(arr[mid:])
    merge(arr[:mid], arr[mid:])

merge_sort(l)
print("List after using Merge Sort: ", end="")
print(l)