""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.


def sort_half(alist):
    # pass
    # split a list into two lists
    mid = len(alist) // 2
    left_half = alist[:mid]
    right_half = alist[mid:]

    # left_half ascending
    for i in range(len(left_half) - 1):
        min_value = i
        for j in range(i + 1, len(left_half)):
            if left_half[j] < left_half[min_value]:
                min_value = j

        if left_half[i] > left_half[min_value]:
            temp = left_half[i]
            left_half[i] = left_half[min_value]
            left_half[min_value] = temp

    # right_half descending
    for k in range(len(right_half) - 1):
        max_value = k
        for l in range(k + 1, len(right_half)):
            if right_half[l] > right_half[max_value]:
                max_value = l

        if right_half[k] < right_half[max_value]:
            temp = right_half[k]
            right_half[k] = right_half[max_value]
            right_half[max_value] = temp

    return left_half + right_half

# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    # pass
    merged_list = A + B
    for i in range(len(merged_list) - 1):
        min_value = i
        for j in range(i + 1, len(merged_list)):
            if merged_list[j] < merged_list[min_value]:
                min_value = j

        if merged_list[i] > merged_list[min_value]:
            temp = merged_list[i]
            merged_list[i] = merged_list[min_value]
            merged_list[min_value] = temp

    return merged_list

# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    # pass
    for i in range(len(mylist)):
        if mylist[i] < 0:
            mylist[i] = 0

    return mylist