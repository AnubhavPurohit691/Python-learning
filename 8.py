#polymorphism

class Animal:
    def speak(self):
        print("animal speaking")

class Dog(Animal):
    def speak(self):
        print("dog speaking")
        