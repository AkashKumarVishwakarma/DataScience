## inbuilt function

# print("Hello, how have you been?") 


## user defined function

# def greet():
#     print("Hello, how have you been?")

# greet()
# greet()


# function with parameters

# def add(a, b):
#     return a + b

# result = add(5, 3)
# print("The sum is:", result)



# function with default parameters

# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# greet()  # Output: Hello, Guest!
# greet("Akash")  # Output: Hello, Akash!


# function with variable-length arguments

# def multiply_all(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total

# result = multiply_all(1, 2, 3, 4)
# print("The total product is:", result)  # Output: The total product is: 24


# function with keyword arguments

# def display_info(name, age):
#     print(f"Name: {name}, Age: {age}")

# display_info(age=25, name="Akash")  # Output: Name: Akash, Age: 25



def palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse

input_string = input("Enter a string: ")
if palindrome(input_string): print("The string is a palindrome.")
else: print("The string is not a palindrome.")





