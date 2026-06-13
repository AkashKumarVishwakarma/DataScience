# def decorate(func):
#     def wrapper():
#         print("I will print my self before the fuction hello")
#         func()
#         print("I will print after the fuction ")
#     return wrapper


# @decorate
# def hello():
#     print("hello I am akarsh vyas")

# hello()

#**************************************************

def decorate(func):
    # def wrapper(a,b):
    def wrapper(*args):
        print("the addition to your numbers are ")
        func(*args)
        print("thankyou I hope you liked it ")
    return wrapper

@decorate
def addition(a,b,c):
    print(f"your total is {a+b+c} ")

addition(12, 67, 11)