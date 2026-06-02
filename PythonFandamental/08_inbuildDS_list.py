# list are mutable and string are immutable. We can create a list using square brackets [] or using the list() constructor.

# s = "hello"
# print(s, type(s))
# s[0] = 'H'  # TypeError: 'str' object does not support item assignment
# print(s)


#**************************************************************************************

# Implemanting list using square brackets []

# a = [12, 15, 20, 25, 30]
# print(a, type(a))
# b = list(range(1, 11))
# print(b)

# c = list('Hello')
# print(c, type(c))
# d = list((1, 2, 3, 4, 5))
# print(d, type(d))
# e = list({1, 2, 3, 4, 5})
# print(e, type(e))

# f = list({'a': 1, 'b': 2, 'c': 3})
# print(f, type(f))
# g = list({'a': 1, 'b': 2, 'c': 3}.items())
# print(g, type(g))
# h = list({'a': 1, 'b': 2, 'c': 3}.values())
# print(h, type(h))
# i = list({'a': 1, 'b': 2, 'c': 3}.keys())
# print(i, type(i))

# hetrogeneous list

j = [1, 2.5, 'hello', [1, 2, 3], (4, 5), {'a': 1, 'b': 2}, print(23), None]
print(j, type(j))






