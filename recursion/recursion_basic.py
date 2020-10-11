# iterative way (loops)
def print_stars(n: int):
    for i in range(n):
        print("*", end="")


# recursive way (without loops)
def print_stars_recur(n: int):
    # assume that n >= 1
    # base case (trivial case)
    if n == 1:
        print("*", end="")

    # recursive case
    # (you do a little bit of work yourself,
    #  and call the same function for the rest of the work)
    else:
        print("*", end="")
        print_stars_recur(n - 1)


# factorial (iteratively)
def factorial(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i  # res = res * i
    return res


# factorial (recursively)
def factorial_recur(n: int) -> int:
    # base case
    if n == 0:
        return 1
    # recursive case
    return n * factorial_recur(n - 1)


# power (iteratively)
def power(base, exp):
    # Assume that exp >= 0
    res = 1
    for _ in range(exp):
        res *= base
    return res


# power (recursively)
def power_recur(base, exp):
    # base case
    if exp == 0:
        return 1
    # recursive case
    return base * power_recur(base, exp - 1)


# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...
# fibonacci n'th sequence (iteratively)
# Time Complexity: O(n)
def fibonacci(n: int) -> int:
    f = 1
    s = 1
    for _ in range(n - 1):
        f, s = s, f + s
    return f


# fibonacci (recursively)
# assume that n >= 1
# Time Complexity: O(2^n)
def fibonacci_recur(n: int) -> int:
    # base case
    if n == 1 or n == 2:  # n <= 2
        return 1
    # recursive case
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


# Leetcode 1137
# Nth Tribonacci Number
# 0, 1, 1, 2, 4, 7, 13, 24, 44, ...
# T0 = 0, T1 = 1, T2 = 1
# Tn = Tn-1 + Tn-2 + Tn-3 (for n >= 0)
#
# tribonacci(4) -> 4
# tribonacci(25) -> 1389537
#
# Time Complexity: O(3^n)
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(tribonacci(4))
print(tribonacci(25))


# (optional) how to improve? -> dynamic programming (memoization)
# Time Complexity: O(n)
def tribonacci_improved(n: int) -> int:
    if n == 0:  # edge case
        return 0

    t0 = 0
    t1 = 1
    t2 = 1
    for _ in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2

    return t2


print(tribonacci_improved(25))