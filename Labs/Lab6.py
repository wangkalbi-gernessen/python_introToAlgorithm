""" Primes, GCD, LCM """
import math

def is_prime(n):
    """ Check if n is prime """
    # pass
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Reference is as follows.
# https://www.edureka.co/blog/gcd-in-python/
def gcd(a, b):
    """ GCD of a and b """
    # pass
    while b > 0:
        a, b = b, a % b
    return a

# print(gcd(16, 8))

def lcm(a, b):
    """ LCM of a and b """
    # pass
    return (a * b) // lcm_helper(a, b)

def lcm_helper(a, b):
    # output gcd
    while b > 0:
        a, b = b, a % b
    return a



def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    # pass
    result = []
    if n == 1:
        return False
    for i in range(2, n + 1):
        if prime(i):
            result.append(i)
    return result

def prime(num: int) -> int:

    if num <= 1:
        return False
    else:
        for j in range(2, num):
            if num % j == 0:
                return False
        return True