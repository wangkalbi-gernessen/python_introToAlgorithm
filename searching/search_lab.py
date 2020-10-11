# search_lab.py
# In this lab, you will be using two searching algorithms we covered in class to
# search for a word in dictionary. Compare the performance for each algorithm.
# You will have to output the number of steps for both algorithms when used for
# searching for the same word. (case-insensitive)
# Your output should look like this.

# Demo output
# Search word: {"orange"}
# Linear Search: found at {0}, took {0} steps
# Binary Search: found at {0}, took {0} steps

from searching.linear_search import *
from searching.binary_search import *

with open("words") as f:  # open the file (words)
    lines = f.readlines()  # read all lines as a list of lines

    # strip off the newline character for each word in the list
    # "list comprehension" (syntax) - python specific
    # stripped = []
    # for line in lines:
    #     stripped.append(line.strip().lower())
    lines = [line.strip().lower() for line in lines]

    target = input("Search word: ").lower()
    li = linear_search(lines, target)
    bi = binary_search(lines, target)

    print(f"Linear Search: found at {li[0]}, took {li[1]} steps")
    print(f"Binary Search: found at {bi[0]}, took {bi[1]} steps")