#comparision operator

a=5
b=10
result = a==b
print(result) 

result=a!=b
print(result)

#<,>,<= ,>= this all are comparision operator

#logical operators

print(True and True) # & we can use this
print(True or True)
print( not True)# it will make false

# conditonal statement

x=-1
if x>=0:
    print("x is positive")
elif x<0 :
    print("negative")

# loops
# for integer
for i in range(5):
    print(i)

for i in range(2,8): #start and end end will be not included
    print(i)

for i in range(2,8, 3): # last is step to skip 3 numbers and it will do in every step
    print(i)

    # to iterate string
word="python"
for char in word:
    print(char)

count=1
while count<5:
    print("helloworld")
    count+=1

password=""
while len(password)<8:
    password=input("Enter a password")

print("password set successfully!")

#None
choice = None # none is null in js