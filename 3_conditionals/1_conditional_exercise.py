# Exercise
# Write a program that takes an user input for an exam mark, and prints
# the grade for that mark - according to the following scheme:
#
#
#   Mark      Grade
#   >= 90       A
#  [80-90)      B
#  [70-80)      C
#  [60-70)      D
#    < 60       F
#
#
# The square and round brackets denote closed and open intervals(range).
# A closed interval includes the number, and open interval excludes it.
# Test your program by print the mark and the grade for a number of different marks.

# mark = int(input("Please put your score: "))
#
# if mark >= 90:
#     print("A")
# elif 80 <= mark < 90:
#     print("B")
# elif 70 <= mark < 80:
#     print("C")
# elif 60 <= mark < 70:
#     print("D")
# else:
#     print("F")


# country = input("Input your favorite country: ")
#
# if country == "Japan":
#     print("Japanese")
# elif country == "Spain":
#     print("Spanish")
# else:
#     print("Other languages")

# 3. 11 Excercises
# Hours: 45
# Rate: 10
# Pay: 475.0

rate = 10
hour = int(input("Hours: "))
regular_amount = 40 * rate

if hour > 40:
    rate *= 1.5
    print(regular_amount + ((hour - 40) * rate))
else:
    print(regular_amount)
