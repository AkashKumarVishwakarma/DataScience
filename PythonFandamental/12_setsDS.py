# s = {}
# print(type(s))

# #implementation of set
# s = {1, 2, 3, 4, 5}
# print(s)
# print(type(s))


# # mutable & Unorderd

# s = {1, 2, 3, 4, 5}
# # s[1] = 10  # This will raise a TypeError because sets do not support indexing
# s.add(6)  # This will add 6 to the set
# print(s)


# # sets do not maintain order
# s = {5, 4, 3, 2, 1}
# print(s)  # Output may not be in the order you defined
# print(type(s))

# # Hetrogenous
# a = {1, 2, 3, 4, 5, 5.5, print(), "hello"}
# print(a)
# print(type(a))

# # sets do not allow duplicates
# b = {1, 2, 4, 5, 3, 3, 2, 1}
# print(b)
# print(type(b))

# # set travesell
# a = {1, 2, 3, 4, 5, 5.5, print(), "hello"}
# for item in a:
#     print(item)
# print(type(a))


# set methods
s = {1, 2, 3, 4, 5}

# s.add(10)  # Add an element to the set
# s.add(0)  # Add an element to the set
# print(s)

# s.remove(2)  # Remove an element from the set
# print(s)

# s.discard(6)  # Remove an element from the set, but does not raise an error if the element is not found
# print(s)

# s.pop()  # Remove and return an arbitrary element from the set
# print(s)

# s.clear()  # Remove all elements from the set
# print(s)



a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# # union
# print(a | b)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# s = a.union(b)
# print(s)

# # intersection
# print(a & b)  # Output: {4, 5}
# s = a.intersection(b) 
# print(s)

# # difference
# print(a - b)  # Output: {1, 2, 3}
# s = a.difference(b)
# print(s)

# # symmetric difference
# print(a ^ b)  # Output: {1, 2, 3, 6, 7, 8}
# s = a.symmetric_difference(b)
# print(s)



# compound assignment operators
# a |= b  # Union update
# print(a)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# a &= b  # Intersection update
# print(a)  # Output: {4, 5}

# a -= b  # Difference
# print(a)  # Output: {1, 2, 3}

a ^= b  # Symmetric difference
print(a)  # Output: {1, 2, 3, 6, 7, 8}







