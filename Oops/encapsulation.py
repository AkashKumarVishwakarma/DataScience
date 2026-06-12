# class Factory:
#     a = "pune"
#     def show(self):
#         print("hello i am a pune factory")
# obj = Factory()
# print(obj.a)
# obj.a = "Bhopal"
# print(obj.a)

##************************************************************

class Factory:
    a = "Public"
    _a = "Protected"
    __a = "Private"

    def show(self):
        print("Hello i am a Public  method. ")
    def _show(self):
        print("Hello i am a Protected  method. ")
    def __show(self):
        print("Hello i am a Private  method. ")
    def showPrivate(self):
        print("Private variable within the class: ", Factory.__a) 

obj = Factory()
print(obj.a)
print(obj._a)
# print(obj.__a)

obj.show()
obj._show()
# obj.__show()

obj.showPrivate()
