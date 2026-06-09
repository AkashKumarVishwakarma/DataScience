# # Write a Python script to  merge two Python dictionaries.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)

# # Write a Python script to check if a given key already exists in a dictionary.
# key_to_check = 'b'
# if key_to_check in dict1:
#     print(f"Key '{key_to_check}' exists in dict1.")
# else:
#     print(f"Key '{key_to_check}' does not exist in dict1.")



# # Write a Python program to sum all the values in a dictionary.

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# total_sum = sum(my_dict.values())
# print(f"The sum of all values in the dictionary is: {total_sum}")


# # Count the frequency of each elements.

# my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# frequency_dict = {}
# for item in my_list:
#     if item in frequency_dict:
#         frequency_dict[item] += 1
#     else:
#         frequency_dict[item] = 1
# print(frequency_dict)


# # Write a Python program to combine two dictionary by adding values for common keys.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

# combined_dict = {}
# for key in set(dict1.keys()).union(set(dict2.keys())):
#     combined_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)
# print(combined_dict)

for i in dict2:
  if i in dict1.keys():
    dict1[i] += dict2[i]
  else:
    dict1[i] = dict2[i]  
print(dict1)

# # Write a Python program to create a dictionary from two lists without losing duplicate values.

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# my_dict = {}
# for key, value in zip(keys, values):
#     if key in my_dict:
#         my_dict[key].append(value)
#     else:
#         my_dict[key] = [value]
# print(my_dict)

