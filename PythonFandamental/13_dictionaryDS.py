# a = {}
# print(type(a))


d = {1:"hello", 2:56, 3:45.6, 4:[1,2,3], 5:(1,2,3), 6:{1:"one", 2:"two"}, 7:True}
# print(d)
# print(type(d))

# # Accessing values from dictionary
# print(d[1])
# print(d[4])
# print(d[6])


# # Adding new key-value pair to dictionary
# d[8] = "new value"
# print(d)

# # Updating value of existing key
# d[2] = 100
# print(d)

# # Deleting a key-value pair from dictionary
# del d[3]
# print(d)


# # dectionary methods

# print(d.keys())
# print(d.values())
# print(d.items())

# d.update({9:"updated value", 10:"another value"})
# print(d)

# del d[1]
# print(d)



# # Looping through dictionary
# for key in d:
#     print(key, d[key])

# # Using items() method to loop through dictionary
# for key, value in d.items():
#     print(key, value)

# d.clear()
# print(d)

#*******************************************************************************

# # Nested dictionary

# nested_dict = {
#     "person1": {"name": "Alice", "age": 30},  
#     "person2": {"name": "Bob", "age": 25},
#     "person3": {"name": "Charlie", "age": 35}
# }
# print(nested_dict)
# # Accessing nested dictionary values
# print(nested_dict["person1"]["name"])

#*********************************************************************************

# a = [1, 2, 3]
# b = a
# b[0] = 100
# print(a)  # Output: [100, 2, 3] # this is known as deep copy

# a = [1, 2, 3]
# b = a.copy()
# b[0] = 100
# print(a)  # Output: [1, 2, 3] # this is known as shallow copy


d = {10:100, 20:200, 30:300}

# d2 = d.copy()
# d2[10] = 1000
# print(d)   # Output: {10: 100, 20: 200, 30: 300} # this is known as shallow copy
# print(d2)  # Output: {10: 1000, 20: 200, 30: 300}

# d2 = d.get(20)
# print(d2)  # Output: 200

# print(d.items())

# print(d.pop(20))  # Output: 200
# print(d)  # Output: {10: 100, 30: 300}

print(d.popitem())  # Output: (30, 300)
print(d)  # Output: {10: 100, 20: 200}








