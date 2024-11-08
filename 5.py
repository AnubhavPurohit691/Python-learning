# In operator

text="anubhav"
result= "a " in text # it also see space

print(result)

#unpacking in list

arr=[12,333,434]
a,b,c=arr
print(a) 

#rest unpacking

a,*b=arr
print(b)

#Tuple 

tuple=(1,2,3)
a,b,c=tuple
print(a)
# in tuple we can not change the value or add or delete

# tuple.remove(2)
# print(tuple)
tu=tuple
tu+=(4,5)
tuple+=(4,5)
print(tuple)
#we can access value of tuple like array or list in python