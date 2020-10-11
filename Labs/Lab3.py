"""
 String, List - Level 2.0
"""


def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    # pass
    return string.count("hi")

    for i in range(len(string) - 1):
        if string[i:i+2] == "hi":
            count += 1
    return count

def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    # pass
    cat_number = string.count("cat")
    dog_number = string.count("dog")
    if cat_number == dog_number:
        return True
    else:
        return False


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    # pass
    import re
    code = re.findall("co.e", string)
    return len(code)

    count = 0
    for i in range(len(string) - 3):
        if string[i:i+2] == "co" and string[i+3] == "e":
            count += 1

    return count


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    # pass

    a_lower = a.lower()
    b_lower = b.lower()
    a_len = len(a_lower)
    b_len = len(b_lower)
    # if a_lower.endswith(b_lower) or b_lower.endswith(a_lower):
    #     return True
    # else:
    #     return False

    if a_len < b_len:
        return b_lower[b_len - a_len:] == a_lower
    else:
        return a_lower[a_len - b_len:] == b_lower


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    # pass

    #
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
        else:
            count += 0

    return count


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    # pass

    max_val = max(nums)
    min_val = min(nums)
    return max_val - min_val


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    # pass

    # count = 0
    # if len(nums) == 0:
    #     return 0
    # else:
    #     if 13 not in nums:
    #         return sum(nums)
    #     else:
    #         for i in range(len(nums)):
    #             if nums[i] == 13:
    #                 continue
    #             elif nums[i] != 13 and nums[i - 1] == 13:
    #                 if nums[i] == nums[0]:
    #                     count += nums[i]
    #                 else:
    #                     continue
    #             else:
    #                 count += nums[i]
    #
    #         return count

    # Following code is Derrick's
    i = 0
    total = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1

    # Following code is mine by using boolean in for loop while
    i = 0  # index number
    count = 0  # amount
    adding_number = True # under addition
    while i < len(nums) - 1:
        if nums[i] == 13 and adding_number:
            adding_number = False
            continue
        elif adding_number:
            count += nums[i]
    return count


print(sum13([1, 5, 13, 2, 4]))



def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    # pass
    # I referred to following URL.
    # https: // stackoverflow.com / questions / 57484048 / codingbat - python - list - 2 - sum67
    # Why is variable start_adding used like this?

    # Following code is mine
    # count = 0
    # start_adding = True  # Boolean is used to add number in for loop
    #
    # if len(nums) == 0:
    #     return 0
    # else:
    #     if 6 not in nums:
    #         return sum(nums)
    #     else:
    #         for i in range(len(nums)):
    #             if nums[i] == 6:
    #                start_adding = False # by switching to False number is not counted
    #             if start_adding:
    #                 count += nums[i]
    #             if nums[i] == 7:
    #                 start_adding = True # by switching to True number is counted
    #
    #         return count

    # Following code is Derrick's
    total = 0
    add_switch = True
    for num in nums:
        if num == 6 and add_switch:
            add_switch = False
            continue
        if num == 7 and not add_switch:
            add_switch = True
            continue
        if add_switch:
            total += num

    return total

print(sum67([2, 7, 6, 2, 6, 2, 7]))


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    # pass

    for i in range(len(nums) - 1):
        if nums[i] == 2:
            if nums[i + 1] == 2:
                return True

    return False
