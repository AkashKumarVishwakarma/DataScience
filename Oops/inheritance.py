class Factorymumbai:        # parent  class / super-class
    a = "I am a Attribute mentioned inside factory"
    def hello(self):
        print("Hello, i am a method mentioned inside Factory")

class Factorypune(Factorymumbai):      # child class / sub-class
    pass

# obj = Factorymumbai()
# print(obj.a)
# obj.hello()

# obj2 = Factorypune()
# print(obj2.a)
# obj2.hello()

#**************************************************************

# #Constructot With Inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(f"hello your name is {self.name} ")


# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f"hello your name is {self.name}, {self.age} ")

# animal = Animal("Lion")
# animal.show()
# person1 = Human("Akash",22)
# person1.show()

#***********************************************************

# # Multiple Inheritance

class Animal:
    def __init__(self, name):
        pass

class Human:
    def __init__(self, name,age):
        pass

class Robots(Human, Animal):
    name3 = "charli123"

obj = Robots() 

