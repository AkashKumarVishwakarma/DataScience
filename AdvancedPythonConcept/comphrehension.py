# # ternary operator
# a = 13
# print("even") if a%2 ==0 else print("Odd")

#*******************LIST COMPHREHENSION**************************
#print & store even number from 1-20 in a list

# l = []
# for i in range(1, 21):
#     if i%2 == 0:
#         l.append(i)
# print(l)

l=[i for i in range(1,21) if i % 2 == 0]
# print(l)


#************************Dictionary Comp**********************

l = {i:i**2 for i in range(1,10)}
# print(l)

#*************************Set Comp********************

unique_even_squares = {x*x for x in range(10) if x%2 == 0}
print(unique_even_squares)
