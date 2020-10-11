# # A while-loop is similar to an if-statement
# # It executes some code if some condition is true.
# # It will continue to execute the code as long as the condition is True
#
# # Syntax
# # while __condition__:
# #     do something
#
# print number from 1 to 10
num = 1
while num <= 10:
    print(num)
    num += 1

# Exercise
# Print all squares from 1 to 99(1,4,9,16,25,...)

num = 1
while num <= 99:
    print(num ** 2)
    num += 1
