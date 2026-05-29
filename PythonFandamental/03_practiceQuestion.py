# #Sum up to n terms.

# n = int(input("Enter the number of terms: "))
# total = 0
# for i in range(1, n+1):
#     total += i

# print("The sum of the first", n, "terms is:", total)



# #Factorial of a number.

# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(f"The factorial of {n} is: {factorial}")



# #Print the sum of all even & odd number in a range separately 

# n = int(input("Enter a number: "))
# even_sum = 0
# odd_sum = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i
# print(f"The sum of even numbers from 1 to {n} is: {even_sum}")
# print(f"The sum of odd numbers from 1 to {n} is: {odd_sum}")


# print all the factors of a number.

n = int(input("Enter a number: "))
print(f"The factors of {n} are: ", end="")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")



