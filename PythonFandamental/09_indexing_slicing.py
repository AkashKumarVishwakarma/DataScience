# # Indexing in python list
# a = [1, 2, 3, 4, 5]
# print(a[0])  # 1
# print(a[1])  # 2
# print(a[2])  # 3
# print(a[3])  # 4
# print(a[-1])  # 5
# print(a[-2])  # 4



# # slicing in python list
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a[0:5])  # [1, 2, 3, 4, 5]
# print(a[5:])  # [6, 7, 8, 9, 10]
# print(a[:5])  # [1, 2, 3, 4, 5]
# print(a[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a[::2])  # [1, 3, 5, 7, 9]
# print(a[1::2])  # [2, 4, 6, 8, 10]
# print(a[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(a[5:2:-1])  # [6, 5, 4



# ************************************************************************************

# Traversing a list using for loop


# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i, end=' ')

# print('\n')    
# for i in range(len(a)):
#     print(a[i], end=' ')

# ****************************************************************************************

#  List Methods
# print(dir(list))

# help(list)


# Implementation of list methods
a = [1, 2, 3, 4, 5]

# a.append(6)
# print(a)  # [1, 2, 3, 4, 5, 6]

# a.insert(0, 0)
# print(a)  # [0, 1, 2, 3, 4, 5, 6]

# a.extend([7, 8, 9, 10])
# print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a.remove(3)
# print(a)  # [1, 2, 4, 5]

# a.remove(0)
# print(a)  # ValueError: list.remove(x): x not in list

# p = a.pop(4) # pop method takes index as arguument and return the value at the index and remove it from the list
# print(a)  # [1, 2, 3, 4]
# print(p)  # 5

# a.reverse()
# print(a)  # [5, 4, 3, 2, 1]

# b = a.copy()
# print(a)  # [1, 2, 3, 4, 5]
# print(b)  # [1, 2, 3, 4, 5]
# a.append(6)
# b.append(7)
# print(a)  # [1, 2, 3, 4, 5, 6]
# print(b)  # [1, 2, 3, 4, 5, 7]


# a.clear()
# print(a)  # []

# print(a.count(3))  # 1
# print(a.count(6))  # 0

# print(a.index(3))  # 2
# print(a.index(6))  # ValueError: 6 is not in list

