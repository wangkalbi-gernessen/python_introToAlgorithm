# What does the code below do? Write a comment explaining each line for Drawing 1.

# n = int(input("Choose a number: "))

# Drawing Example
# for row in range(n):  # for each row
#     for column in range(row+1):  # for each column
#         print('*', end='')  # print without newline at the end
#     print()


# Drawing 1
# YOUR CODE BELOW (feel free to comment out previous drawings to make newer ones more clear)

def draw_1(n: int) -> int:

    for row in range(n):
        print("")
        for blank_left in range(0, n - row - 1, 1):
            print(" ", end="")
        for star in range(0, 2 * row + 1, 1):
            print("*", end="")
        for blank_right in range(n - 1, row, -1):
            print(" ", end="")

draw_1(7)
print("")


# Drawing 2
def draw_2(n: int) -> int:

    for row in range(n):
        print("")
        for column in range(0, n - row, 1):
            print("*", end="")
        for blank in range(0, n - column, 1):
            print("", end="")

draw_2(7)
print("")


# Drawing 3
def draw_3(n: int) -> int:

    for row_top in range(n // 2 + 1):
        print("")
        for star_top in range(0, row_top + 1, 1):
            print("*", end="")

    for row_bottom in range(n // 2):
        print("")
        for star_bottom in range(n // 2, row_bottom, -1):
            print("*", end="")

draw_3(7)
print("")


# Drawing 4
def draw_4(n: int) -> int:
    for top_row in range(n // 2):
        print("")
        for top_left_blank in range(top_row):
            print(" ", end="")
        for top_center_star in range(n - 2 * top_row, 0, -1):
            print("*", end="")
        for top_right_blank in range(top_row):
            print(" ", end="")

    for bottom_row in range(n // 2 + 1):
        print("")
        for bottom_left_blank in range(n // 2 - bottom_row):
            print(" ", end="")
        for bottom_center_star in range(2 * bottom_row + 1):
            print("*", end="")
        for bottom_right_blank in range(n // 2, bottom_row, -1):
            print(" ", end="")

draw_4(7)
print("")


# Drawing 5
def draw_5(n: int) -> int:

    for top_row in range(n // 2):
        print("")
        for top_left_blank in range(n // 2 - top_row):
            print(" ", end="")
        for top_center_star in range(2 * top_row + 1):
            print("*", end="")
        for top_right_blank in range(n // 2, top_row, -1):
            print(" ", end="")

    for bottom_row in range(n // 2 + 1):
        print("")
        for bottom_left_blank in range(bottom_row):
            print(" ", end="")
        for bottom_center_star in range(n - 2 * bottom_row, 0, -1):
            print("*", end="")
        for bottom_right_blank in range(bottom_row):
            print(" ", end="")

draw_5(7)