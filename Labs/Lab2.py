"""
Basic python list problems -- no loops.
"""


def first_last6(nums):
    """
    Given a list of ints, return True if 6 appears as either the first or last element in the list.
    The list will be length 1 or more.
    """
    if len(nums) >= 1:
        if nums[0] == 6 or nums[len(nums) - 1] == 6:
            return True
        else:
            return False
    else:
        return False


def same_first_last(nums):
    """
    Given a list of ints, return True if the list is length 1 or more, and the first element
    and the last element are equal.
    """
    # pass
    if len(nums) >= 1:
        if nums[0] == nums[len(nums) - 1]:
            return True
        else:
            return False
    else:
        return False


def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.
    Both lists will be length 1 or more.
    """
    # pass
    if len(a) >= 1 and len(b) >= 1:
        if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
            return True
        else:
            return False
    else:
        return False


def sum3(nums):
    """
    Given a list of ints length 3, return the sum of all the elements.
    """
    # pass
    sum = 0
    for i in nums:
        sum += i

    return sum


def rotate_left3(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """

    nums.append(nums.pop(0))
    return nums


def reverse3(nums):
    """
    Given a list of ints length 3, return a new list with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.
    """
    # pass
    result = []
    for i in reversed(nums):
        result.append(i)

    return result


def max_ends3(nums):
    """
    Given a list of ints length 3, figure out which is larger, the first or last element in the list,
    and set all the other elements to be that value. Return the changed list.
    """
    # pass

    result = []
    if nums[0] > nums[len(nums) - 1]:
        result.append(nums[0])
        multi_val = result * len(nums)
        return multi_val
    else:
        result.append(nums[len(nums) - 1])
        multi_val = result * len(nums)
        return multi_val


def make_ends(nums):
    """
    Given a list of ints, return a new list length 2 containing the first and last elements from the original list.
    The original list will be length 1 or more.
    """
    # pass
    result = []
    if len(nums) >= 2:
        for i in range(len(nums)):
            if nums[i] == nums[0] or nums[i] == nums[len(nums) - 1]:
                result.append(nums[i])
        return result
    elif len(nums) == 1:
        multi_val = nums * 2
        return multi_val
    else:
        return False


def has23(nums):
    """
    Given an int list length 2, return True if it contains a 2 or a 3.
    """
    # pass
    if 2 in nums or 3 in nums:
        return True
    else:
        return False
