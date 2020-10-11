# """ Guessing Game """
import random
#
#
# 1. Following code my thought.
def guessing_game(target: int) -> int:
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    # your code goes here.
    # print(f"answer: {answer}")

    min = 1
    max = 1000
    steps = 0

    while target != answer:
        steps += 1

        if target < answer:
            print(f"Wrong! Guess count: {steps}")
            min = target + 1
            target = int(input(f"Enter your guess from {min} to {max}: "))
        else:
            print(f"Wrong! Guess count: {steps}")
            max = target - 1
            target = int(input(f"Enter your guess from {min} to {max}: "))

    print(f"You got it! The hidden number is {answer}\n It took you {steps + 1} guess(es)")

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do

if __name__ == '__main__':
    target = int(input(f"Enter your guess from 1 to 1000: "))
    guessing_game(target)



# 2. Following code is Derrick's.

# generate a random integer from 1 to 1000
# def guessing_game(target: int) -> int:
#     answer = random.randint(1, 1000)  class RangeError(Exception):
#
#
#     # your code goes here.
#     # print(f"answer: {answer}")
#
#     lower_bound = 1
#     upper_bound = 1000
#     count = 0
#     found = False
#
#     while not found and lower_bound <= upper_bound:
#         try:
#             guess = int(input(f"Enter your guess from {lower_bound} to {upper_bound}: "))
#             count += 1
#             if guess < lower_bound or guess > upper_bound:
#                 raise RangeError
#             if guess == answer:
#                 print(f"You got it! The hidden number is {guess}")
#                 print(f"It too you {count} guess(es).")
#                 break
#             elif guess > answer:
#                 upper_bound = guess - 1
#             else:
#                 lower_bound = guess + 1
#             print(f"Wrong! Guess count: {count}")
#
#         except RangeError:
#             print(f"Please enter a number from {lower_bound} to {upper_bound}.")
#         except ValueError:
#             print("Invalid Input.")
#
# # https://stackoverflow.com/questions/419163/what-does-if-name-main-do
#
# if __name__ == '__main__':
#     guessing_game()
