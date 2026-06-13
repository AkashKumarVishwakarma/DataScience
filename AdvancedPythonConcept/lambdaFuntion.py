# addition  = lambda a,b : a +b
# print(addition(12, 32)) 


result = lambda a : "even" if a%2 == 0 else "odd"
# print(result(19))

#***********MAP & FILTER ***************************************

a = [1,2,3,4,5]
# result = map(lambda x : x*2, a)
# # print(result)
# print(list(result))


def double(x):
    return x*2
result = map(double,a)
# print(list(result))


#********************************************************************

def even(x):
    if x%2 == 0:
        return True
    else:
        return False
a= [1,2,3,4,5,6,7,8,9]

# result = filter(even, a)

result = filter(lambda x : True if x%2 == 0 else False, a)

print(list(result))