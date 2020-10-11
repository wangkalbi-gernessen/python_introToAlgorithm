""" Group Lab 2 (in-class) Exhaustive Search, Backtracking """
def permutation_helper(word, start):
    if start == len(word):
        print("".join(word))
    for i in range(start, len(word)):
        word = [ch for ch in word]
        word[start], word[i] = word[i], word[start]
        permutation_helper(word, start + 1)
def permutation(word: str):
    """
    Write a recursive function permutation that accepts a string as a parameter
    and outputs all possible rearrangements of the letters in the string.
    The arrangements may be output in any order.
    example)
    permutation("park")
    output: park, pakr, pkar, prak, arpk, aprk, akrp, ...
    :param word: word to permute
    :return: display permutations of a given word
    """
    permutation_helper(word, 0)

permutation("park")


def sum_of_dice(dice: int, desired_sum: int):
    """
    Prints all possible outcomes of rolling the given number of six-sided dice
    that add up to the given desired sum, in {#, #, #} format.
    :param dice: the number of dice
    :param desired_sum: desired sum
    :return: display all possible ways
    example)
    sum_of_dice(2, 7)
    output: {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 1}
    """
    solutions = []
    for i in range(1, 7):
        if desired_sum < i:
            continue
        if desired_sum == i:
            if dice == 1:
                solutions.append([i])
        if desired_sum - i < dice - 1:
            continue
        for solution in sum_of_dice(dice - 1, desired_sum - i):
            solutions.append([i] + solution)
    return solutions

print(sum_of_dice(2, 7))