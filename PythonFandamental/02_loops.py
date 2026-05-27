#RANGE FUNCTION

# a = range(1, 20, 1)
# for i in a:
#     print(i)

# for i in range(20):
#     print(i)

# for i in range(16,1,-1):
#     print(i, end=" ")


# a = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(a, "X", i, "=", a*i)

# *********************************************************
# a = int(input("Enter a number: "))
# for i in range(a, (a*10)+1, a):
#     print(i, end=" ")

 #####################################################################################

# Strings

# a = "AKASH KUMAR"

# for i in range(len(a)):
#   print(a[i], end=" ")

# for i in a:
#     print(i, end=" ")


###############################$$$$$  BREAK & CONTINUE STATEMENT
# for i in range(1, 21):
#   if i == 15:
#     # break
#     continue
#   print(i, end=" ")


#############################$$$$$  ELSE STATEMENT WITH FOR LOOP
for i in range(1, 6):
    if i == 15:
        break
        # continue  // Continue does not execute else block code because it does not terminate the loop.
    print(i, end=" ")

else:
    print("\nLoop completed without break")
