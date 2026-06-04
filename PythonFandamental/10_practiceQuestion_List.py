# # print positive and negative elements from the list

# a = [1, -2, 3, -4, 5, -6]
# for i in a:
#     if i > 0:
#         print(i, end=' ')
# print('\n')
# for i in a:
#     if i < 0:
#         print(i, end=' ')



# # print even and odd elements from the list

# a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     if i % 2 == 0:
#         print(i, end=' ')
# print('\n')
# for i in a:
#     if i % 2 != 0:
#         print(i, end=' ')



# # Mean of List elements

# a = [1, 2, 3, 4, 5]
# sum = 0
# for i in a:
#     sum += i
# mean = sum / len(a)
# print(mean)  # 3.0


# #Find the greatest element and print its index too.

# a = [1, 2, 3, 4, 5]
# max = a[0]
# index = 0 
# for i in range(1, len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i
# print("Greatest element:", max)
# print("Index of greatest element:", index)


# # Find the second greatest element and print its index too.

# a = [1, 2, 3, 4, 5]
# max = a[0]
# second_max = a[0]
# index = 0
# for i in range(1, len(a)):
#     if a[i] > max:
#         second_max = max
#         max = a[i]
#         index = i
#     elif a[i] > second_max and a[i] != max:
#         second_max = a[i]
# print("Second greatest element:", second_max)
# print("Index of second greatest element:", index)


# # check if the list is empty or not

# a = []
# if not a:
#     print("List is empty")
# a = [1, 2, 3]
# if a:
#     print("List is not empty")


# Check if List is sorted or not

# a = [1, 2, 3, 4, 5]
# is_sorted = True
# for i in range(len(a) - 1):
#     if a[i] > a[i + 1]: 
#         is_sorted = False
#         break
# if is_sorted:
#     print("List is sorted")


a = [1, 1, 3, 5, 4]
is_sorted = True
for i in range(len(a) - 1):
    if a[i] > a[i + 1]: 
        is_sorted = False
        break
if is_sorted:
    print("List is sorted")



