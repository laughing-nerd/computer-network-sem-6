a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")
w = input("Enter the value of w: ")
z = input("Enter the value of z: ")

#-------------------------------------------------------------------------------------------
d1 = {
        0: [a,b,c,d],
        1: [x,y,w,z]
}
n=len(d1[0])
l1=d1[0]
l2=d1[1]
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(l1[j]<l1[j+1]):
            temp1 = l1[j]
            temp2 = l2[j]
            l1[j] = l1[j+1]
            l2[j] = l2[j+1]
            l1[j+1] = temp1
            l2[j+1] = temp2
d1.update({0:l1, 1:l2})
print(d1)
#-------------------------------------------------------------------------------------------
d2={}
for i in range(n):
    d2.update( {d1[1][i] : d1[0][i]} )
print(d2)
#-------------------------------------------------------------------------------------------
d3={}
keys = list(d2.keys())
values = list(d2.values())
key1 = keys[1]+keys[2]
key2 = keys[0]+keys[3]
value = values[1]*values[2] + values[0]*values[3]
d3.update( {key1+"+"+key2 : value} )
print(d3)
#-------------------------------------------------------------------------------------------
d={
        1: "y=5",
        2: "x=7",
        3: "z=6",
        4: "w=10"
}
v1 = (int(d[1][2:].strip()) * int(d[2][2:].strip()))
v2 = (int(d[3][2:].strip()) * int(d[4][2:].strip()))
print(v1+v2)
