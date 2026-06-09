# # print("Start")
# # a = 10/0
# # print("End")

# # # Solve the above problem using try and except block.
# # try:
# #     print("Start")
# #     a = 10/0
# #     # a = 10/5
# #     print("End")
# # # except ZeroDivisionError:
# # except Exception as err:
# #     print(f"Sorry there is an error as {err}")

# # print("ok I have done the division.")


# # # Unsupported operand type error.

# # a = input("Enter a number: ")
# a = int(input("Enter a number: "))  # to see else block code

# try:
#     print(10/a)
# except Exception as err:
#     print(f"Sorry there is an error as {err}")
# else:
#     print("Good there is no Exception.")
# finally:   # finally block always run no matter exception handeled or not
#     print("I will run no matter what")
# print("ok I have done the division.")    


# # raise Keyword

# age  = int(input("Enter your agr: "))
# if (age < 10 or age > 18):
#     raise ValueError("Your age must be between 10 & 18")
# else:
#     print("Wellcome to the club")

# print("The club will start soon")   
#  

#*************************************************************************
try:
    age  = int(input("Enter your agr: "))
    if (age < 10 or age > 18):
        raise ValueError("Your age must be between 10 & 18")
    else:
        print("Wellcome to the club")
except Exception as err:
    print(f"an error occured as {err}")

print("The club will start soon") 