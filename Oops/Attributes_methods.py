class Animal:
    name = "Lion"  # Class Attributes

    def __init__(self, age):
        self.age = age  # instance Attribute

    def show(self):  # instance methods
        print(f"how are your age is {self.age} ")

    @classmethod
    def hello(cls):
        print(f"how are you brother. i am class method ")

    @staticmethod
    def static():
        print("how are you this is static method. ")


obj = Animal(12)

# obj.show()
# obj.hello()
obj.static()