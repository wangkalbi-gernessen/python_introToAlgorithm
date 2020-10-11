# Loops - to repeat code
#
# For loops are used to iterate over a given sequence.
# On each iteration, the variable (loop variable) defined in
# the for loop will be assigned to the next value (sequence)

# Numbers
# range([start,] end[, steps])

# range(end) - 0 <= < end
for i in range(10):  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(i)

# range(start, end) - start <= < end
for i in range(1, 11):
    print(i)

# range(start, end, steps) - 0 <= < end (skip steps every iteration)
for i in range(1, 101, 2):
    print(i)

# print 100, 99, 98, ..., 3, 2, 1
for i in range(100, 0, -1):
    print(i)

# print 1 2 3 4 5 6 7 8 9 10
# for i in range(1, 11):
#     print(i, end=" ")

# Exercise
# 1. print all odd numbers from 0 to 100
for i in range(101):
    if i % 2 != 0:
        print(i)
    # pass

# 2. print all even numbers from 0 to 100
for i in range(101):
    if i % 2 == 0:
        print(i)
    # pass


# Strings: a sequence of characters
school = "Cornerstone"
for i in school:
    print(i)

# Count the number of vowels
# Vancouver
city = "vancouver"
count = 0
for i in city:
    if i in "aiueoAIUEO":
        count += 1

print(count)