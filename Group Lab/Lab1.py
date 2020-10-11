""" group exercises 2 """
import math

# Write a recursive function printBinary that accepts integer and
# prints that number's representation in binary (base 2)
#
# Examples:
# print_binary(2)    prints 10
# print_binary(7)    prints 111
# print_binary(12)   prints 1100
# print_binary(42)   prints 101010
# print_binary(-500) prints -111110100
# def print_binary(num):
    # pass
#     if num < 0:
#         return -(subfunction(num))
#     elif num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return num % 2 + 10 * print_binary(num // 2)
#
# def subfunction(num):
#     if num == 0:
#         return 0
#     elif num == -1:
#         return 1
#     else:
#         return (num % 2) + 10 * subfunction(math.ceil(num / 2))
#
# print(print_binary(-500))

# print binary
def print_binary(num: int):
    print(print_binary_helper(num))

def print_binary_helper(num: int) -> str:
    if num < 0:
        return "-" + print_binary_helper(num * -1)
    if num == 0:
        return ""
    if num % 2 == 0:
        return print_binary_helper(num // 2) + "0"
    else:
        return print_binary_helper(num // 2) + "1"

# print_binary(2)
# print_binary(7)
# print_binary(12)
# print_binary(42)
# print_binary(-500)


# Write a recursive function evaluate that accepts a string
# representing a math expression and computes its value.
# - The expression will be "fully parenthesized" and will
#   consist of + and * on single-digit integers only.
# - You can use a helper function. (Do not change the original function header)
# - Recursion
#
# evaluate("7")                 -> 7
# evaluate("(2+2)"              -> 4
# evaluate("(1+(2*4))"          -> 9
# evaluate("((1+3)+((1+2)*5))") -> 19

# recursively evaluate the same pattern (left op right)
def eval_helper(expr: str, i: int) -> int:
    # base case
    if expr[i].isdigit():
        return int(expr[i])
    # recursive case
    else:
        # (left-expr op right-expr)
        i += 1  # skip '('
        left = eval_helper(expr, i)
        i += 1  # skip left operand
        op = expr[i]
        i += 1
        right = eval_helper(expr, i)
        i += 1  # skip ')'
        if op == '*':
            return left * right
        else:
            return left * right

def evaluate(expr: str) -> int:
    # pass
    return eval_helper(expr, 0)

print(evaluate("(2+2)"))


# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 10 to 99 (two digits)
# print_decimal(3)  prints from 100 to 999 (three digits)


# Following code is our answer.
# We were trying to find solution, but we wasn't able to solve with recursive function.

# def print_range(start, end):
#     while start <= end:
#         print(f"{start} ", end="")
#         start += 1
#
# def print_decimal(digits):
#     # pass
#     # base case
#     if digits == 0:
#         return 0
#     elif digits == 1:
#         print_range(0, 9)
#     else:
#         print_range(10 ** (digits - 1), 10 ** digits - 1)
#
# print_decimal(3)

# Following code is Derrick's
def print_decimal(digits: int):
    print_decimal_helper(digits, "", "")

def print_decimal_helper(digits: int, sofar: str, indent: str):
    print(f"{indent}print_decimal_helper({digits}, {sofar})")
    if digits == 0:  # base case, no more digit to print
        print(sofar)
    else:  # recursive
        for i in range(10):
            if sofar != "0":
                print_decimal_helper(digits - 1, sofar + str(i), indent + "    ")

print_decimal(3)
