# Bubble Sort - "Bubbling" up the largest element to the right!
# (pseudo-code)
#
# for each scan from 1 to n-1
#   compare two adjacent elements for all
#   if the first element is greater than the second element
#     swap two elements
#
# Time Complexity: O(n^2)


def bubble_sort(items: [int]):
    steps = 0
    for scan in range(len(items) - 1):
        for i in range(len(items) - 1 - scan):
            steps += 1
            if items[i] > items[i+1]:
                # items[i], items[i+1] = items[i+1], items[i]
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items
    print(f"steps: {steps}")

print(bubble_sort([3, 5, 1, 6, 2, 4]))

def bubble_sort_improved(items: [int]):
    steps = 0
    for scan in range(len(items) - 1):
        swapped = False
        for i in range(len(items) - 1 - scan):
            steps += 1
            if items[i] > items[i+1]:
                swapped = True
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

        if not swapped:
            break
    print(f"steps: {steps}")

# test
import random

alist = random.sample(range(1, 500), 300)
alist1 = alist[:]
bubble_sort(alist)
bubble_sort_improved(alist1)
print(alist)



def bubble_practice(items: [int]) -> int:
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j + 1] = temp
    return items

arrays = [5, 1, 6, 2, 4, 7, 3]
print(bubble_practice(arrays))
