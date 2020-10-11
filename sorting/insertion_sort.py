def insertion_sort(items: [int]) -> int:
    for i in range(1, len(items)):
        temp = items[i]  # keep head value(i)

        j = i  #
        while j - 1 >= 0 and temp < items[j - 1]:
            items[j] = items[j - 1] # exchange value
            j -= 1

        items[j] = temp

    return items

arrays = [4, 3, 2, 10, 12, 1, 5, 6]
print(insertion_sort(arrays))