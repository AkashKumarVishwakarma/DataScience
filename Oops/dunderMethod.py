class Animal:
    def __init__(self, name, age):
        self.name=name
        self.age = age
        # print(f"helo, hey! {name} ") 
    def __str__(self):
        # print("Hello how are you ")
        return f"hello how are you and your name is {self.name}"
    # def __add__(self,other):
    #     return f"Your sum of ages are {self.age + other.age} "

    def __add__(self,other):
        sum = 0;
        for i in other:
            sum = sum + i.age
            
        return f"Your sum of ages are {self.age + sum} "

obj = Animal("Lion",12)
obj2 = Animal("dolphin",14) 
obj3 = Animal("tiger",34)

# print(obj)
print(obj + (obj2,obj3))