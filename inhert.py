# Simple inheritance

# # Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# # # Derived class
class Dog(Animal):                      # here, name of class is "Dog" / as a Argument we are passing -->Animal (class)

    def speak(self):                    # this is a method 
        print(f"{self.name} barks.")    # this is using a Attribute called -->self.name 
 
# # # Create an instance of Animal i.e creating a Object 
animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound.

# # # Create an instance of Dog
dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks.

#   ::::::NOTE::::::::::
# class Dog(Animal):  --> In "Dog" class we are Inheriting "Animal" class   
# so now from Dog class -->what ever object -->it will be able to access the atribute of Amimal class i.e [parent class]
# And also it can inherit the method of Parent class 

# Super Keyword

# Super

# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# # Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()  # if we want to use parent attributes also then we use Super Keyword # Full constructor is called 
        self.breed = breed

    def speak(self):
        super().speak()  # Call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

# # Create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()
# Output:
# Buddy makes a sound.
# Buddy barks. It is a Golden Retriever.