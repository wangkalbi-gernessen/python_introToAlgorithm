while True: #This makes your code repeat forever, to make it easier for you to keep testing it out with different values

    # You may assume the input will be valid
    # e.g. Your program does not have to work if someone gives an n that is
    #      bigger than the total number of digits in number. Your code must
    #      only work correctly for valid input.
    number = int(input("Please give an integer number: ")) # this asks the user for input and then stores the user input as an int into our variable
    n = int(input("Which position's digit do you want? "))

    print(".....YOUR CODE HERE......") # TO DO: Replace the filler text here with your code




    def digit_value(number: int, n: int) -> int:
        return number // 10 ** (n) % 10

        # By dividing 10 the first of the number is removed
        # By dividing 10 the first of the number appears as remainder
        # if n == 1:
        #     print(number % 10)
        # elif n >= 2:
        #     while n > 0:
        #         number = number // 10
        #     print(number % 10)

        # simpliest solution
        # s = str(number)
        # print(s[len(s) - n])

    print(digit_value(number, n - 1))

# https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python)