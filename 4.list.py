numbers=[1,2,3,4]
print(numbers[2:4])# 3 is not included

numbers[2]=8
print(numbers)
del numbers[2]#to delete
print(numbers)  

#1D list

a=[1,2,3,4,5]

#2D list

b=[[1,2,3],[4,5,6],[7,8,9]]

#3D list    

c=[
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
,[
    [10,11,12],
    [13,14,15],
    [16,17,18]
    ]
]

#append
yolist=[5,4,4]
yolist.append(6)
print(yolist)

#extend
yolist.extend([7,8])
print(yolist)

#insert
yolist.insert(0,0)
print(yolist)

#remove 
yolist.remove(4)
print(yolist)# it doesn't start with 0

#pop
yolist.pop()
print(yolist)

#sort
yolist.sort()
print(yolist)

#reverse
yolist.reverse()
print(yolist)


for element in yolist:
    print(element)

for i in range(len(yolist)):
    print(yolist[i])

i=0
while i<len(yolist):
    print(yolist[i])
    i+=1

#clear  
yolist.clear()
print(yolist)


