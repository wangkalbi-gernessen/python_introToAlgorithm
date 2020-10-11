# is prime.py

import math
import time

def is_prime_naive(n: int) -> bool:
    """
    Check whether n is prime or not O(n)
    :param n:
    :return:
    """
    if n == 1:
        return False

    for i in range(2, n):   # n
        if n % i == 0:
            return False

    return True


# 2 to sqrt(n)
# n = 100
# sqrt(n) = 10

# def is_prime(n: int) -> bool:
# """
# Check whether n is prime or not O(sqrt(n))
# """
#
#     if n == 1:
#         return False
#
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#
#     return True

def generate_prime_list(n: int):
    """
    Returns a list of prime numbers from 2 to n
    :param n: upper bound
    :return: a list of prime numbers
    """

    prime_list = []
    for i in range(2, n + 1):
        if is_prime_naive(i):
            prime_list.append(i)

    return prime_list

start_time = time.time()
generate_prime_list(1000000)
end_time = time.time()
print(f"{end_time - start_time} seconds")