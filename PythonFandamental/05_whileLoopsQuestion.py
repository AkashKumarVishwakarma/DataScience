# # separate each digit of a number and print it on the new line.

# n = int(input("Enter a number: "))
# while n > 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10



# # Accept a number and print its reverse.

# n = int(input("Enter a number: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print("Reversed number:", reverse)


# # Accept a number and check if it is a palindrome.

# n = int(input("Enter a number: "))
# original = n
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# if original == reverse:
#     print("The number is a palindrome.")
# else:    print("The number is not a palindrome.")
