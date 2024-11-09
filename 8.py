#polymorphism
#it means many forms
class Animal:
    def speak(self):
        print("animal speaking")

class Dog(Animal):
    def speak(self):
        print("dog speaking")
        # this will override the speak function

#Method Overloading

# mehod overloading in pyhon involves creating multiple methods with the same name but different parameters.called as compile time polymorphism


class Mathoperations:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c


add_to_numbers=Mathoperations()
print(add_to_numbers.add(1,2,3))

#Encapsulation 
#it means hiding the data
#here no public or private modifier is there just like other language

class Myclass:
    def __init__(self,x):
        self.x=x

    #this method is public
    def get_x(self):
        return self.x


obj=Myclass(10)  
print(obj.get_x())

#Protected modifier this are convension 
class Myclass1:
    def __init__(self,x):
        self._x=x

    #this method is public
    def get_x(self):
        return self._x


obj=Myclass(10)  
print(obj.get_x())
#Private modifier this are convension here we use __underscore
#this things developer only know

# ------- Private Modifier
# In Python, attributes and methods that start with double underscores __ are considered "private." This means they are not accessible from outside the class. However, Python does not enforce this access restriction strictly;


class MyClass:
    def __init__(self, x):
        self.__x = x  # 👈 This attribute is private

    def get_x(self):
        return self.__x  # 👈 This method is public


obj = MyClass(10)
print(obj.get_x())  # 10
# Accessing a private attribute (not recommended, and name-mangled)
print(obj._MyClass__x) 