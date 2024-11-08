from datetime import datetime

print(datetime.now())
date=datetime(2025,4,15)
print(date)

#classes

class Person:
    #constructor is init
    def __init__(self,name,age): #self is nessary it needs 1 argument 
        self.name=name
        self.age=age

        #self tell that this name is belongs to this class
    def display(self):
        print(self.name)
        print(self.age)


p1=Person("anubhav",20)
p1.display()

#static variable in class

class Car:
    wheels=4
    def __init__(self,name):
        self.name=name

    def display(self):
        print(self.name)
        Car.wheels+=1

c1=Car("bmw")
c1.display()
print(c1.wheels)

#inheritance
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)

class Dog(Animal):
    def bark(self):# here this can't be constructor
        print("dog constructor")

h1=Dog("anubhav121",202121)
h1.display()

class Cat(Animal):
    def __init__(self, bark,name,age):
        super().__init__(name, age)
        self.bark=bark
        print(self.bark)


p=Cat("meow","afjskfs",12)
p.display()