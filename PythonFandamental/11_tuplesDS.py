# # immutable
# t = (1, 2, 3, 4, 5)
# print(t)
# # t[0] = 100 # TypeError: 'tuple' object does not support item assignment

# # tuple packing
# t1 = 1, 2, 3, 4, 5
# print(t1)
# print(type(t1))



# # nested tuple
# t2 = (1, 2, (3, 4), 5)
# print(t2)


# hetrogenous
# a = (1, 2, 3, 4, 5, 5.5, print(), "hello")
# print(a)
# print(a[2])



# # tuple unpacking
user_data = ("Alice", "Admin", "USA", "English", 28)

# # Extract first two elements, group the rest
# name, role, *other_details = user_data

# print(name)           # Output: Alice
# print(role)           # Output: Admin
# print(other_details)  # Output: ['USA', 'English', 28]

# # Extract first and last elements, group the middle
# name, *middle_details, age = user_data  

# print(name)             # Output: Alice
# print(middle_details)   # Output: ['Admin', 'USA', 'English']
# print(age)              # Output: 28


# user_ages = {"Alice": 25, "Bob": 30}
# for name, age in user_ages.items():
#     print(f"{name} is {age} years old.")

#**********************************
# a = (1)   # Output: <class 'int'> ##### because it treats as tuple unpaking
# a = (1,)
# print(type(a))  
#***************************************

def get_min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = get_min_max([3, 1, 4, 1, 5])
print(f"Lowest: {lowest}, Highest: {highest}")


# # Tuples Methods

# t = (1, 2, 3, 4, 5, 2)
# print(t.count(2))  # Output: 2
# print(t.index(3))  # Output: 2
