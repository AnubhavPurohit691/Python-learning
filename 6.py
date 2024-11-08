#sets are collection of unique elements
#sets are unordered
#sets are mutable
#sets are iterable
#sets are unchangeable
myset={1,2,3,4,5}
print(myset)

set1=set({1,2,3,4,5}) 
print(set1)
myset.add(6)
print(myset)
myset.update({7,8,9})
print(myset)


#FUNCTIONS
def greet(name="anubhav"):#default argument
    print("hello",name)
    print("good morning")


#CALLING
greet("nasty")
greet()

#lambda function
x=lambda a:a+10
print(x(5)) # this is short function as we have only one line