# # Accept a number and check if it a perfect number or not. A number whose sum of factor is equal to the number itself.

# n = int(input("check your number is  perfect or not :- "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         # print(i, end=" ")
#         sum += i

# print(f"The sum of factors of {n} is: {sum}")
# if sum == n:
#     print("perfect number")
# else:
#     print("not a perfect number")



## check if a number is prime or not.

# n = int(input("check your number is  prime or not :- "))
# is_prime = True
# if n <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("prime number")
# else:
#     print("not a prime number")



# # print all the prime numbers in a range.
# n = int(input("Enter a number: "))
# print(f"The prime numbers from 1 to {n} are: ", end="")
# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")


# # reverse a string without using in build functions.

# s = input("Enter a string: ")
# reversed_string = ""
# for char in s:
#     reversed_string = char + reversed_string
# print("Reversed string:", reversed_string)


# # check if a string is palindrome or not.

# s = input("Enter a string: ")
# reversed_string = ""
# for char in s:
#     reversed_string = char + reversed_string
# if s == reversed_string:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")



# Count all letters, digits, and special symbols from a given string.
    # Given: str1 = "P@#yn26at^&i5ve"
    #Expected Output:
      #LETTERS  : 8
      # DIGITS  : 3
      # SYMBOLS : 4

s = "P@#yn26at^&i5ve"
letters = 0
digits = 0
symbols = 0
for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"LETTERS  : {letters}")
print(f"DIGITS   : {digits}")
print(f"SYMBOLS  : {symbols}")



