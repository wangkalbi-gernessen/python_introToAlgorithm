import random

# Selection Sort
# pseudo-code
# find the min element (linear-search)
# swap the min element with starting index(scan)

l = [7, 4, 5, 2, 1, 9, 10, 3]

# first solution
# how to find the index of the min number?
# min_value = l[0]
# index_min = 0
# for i in range(len(l)):
#     if l[i] < min_value:
#         index_min = 1



# print(l.index(min(l)))

# second solution
# def selection_sort(items: [int]):
#     for scan in range(len(items) - 1):
#         min_index = scan
#         for i in range(scan + 1, len(items)):
#             if items[i] < items[min_index]:
#                 min_index = i
#
#         # swap
#         if min_index != scan: # if False, swapping the same value
#             temp = items[scan]
#             items[scan] = items[min_index]
#             items[min_index] = temp



# if __name__ == '__main__':
#     list_items = random.sample(range(1, 20), 7)
#     selection_sort(list_items)
#     print(list_items)




# Following code is my thought.
def selection_sort_practice(items: [int]) -> int:
    for scan in range(len(items) - 1):
        min_value = scan
        for j in range(scan + 1, len(items)):
            if items[min_value] > items[j]:
                min_value = j

        if items[min_value] < items[scan]:
            temp = items[scan]
            items[scan] = items[min_value]
            items[min_value] = temp
    return items

arrays = [5, 1, 6, 2, 4, 7, 3]
print(selection_sort_practice(arrays))

