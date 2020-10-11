""" Final Exam V3 """


# please submit your python file upon completion.

def is_anagram(s: str, t: str) -> str:
    """
    An anagram is a word or phrase formed by rearranging the
    letters of a different word or phrase, typically using all
    the letters exactly once.

    Given two strings s and t, write a program to
    determine if t is an anagram of s.
    You may assume that the string contains only lowercase alphabets.

    e.g.
    is_anagram("anagram", "nagaram") -> True
    is_anagram("rat", "car") -> False
    is_anagram("listen", "silent") -> True
    is_anagram("", "") -> True
    is_anagram("h", "e") -> False

    :param s: string
    :param t: string
    :return: True if s is an anagram of t, otherwise False
    """
    # pass
    s_list = list(s.lower())
    t_list = list(t.lower())
    if is_anagram_sort_s(s_list) == is_anagram_sort_t(t_list):
        return True
    else:
        return False

def is_anagram_sort_s(s_list):
    for scan_s in range(len(s_list) - 1):
        min_value = scan_s
        for j in range(scan_s + 1, len(s_list)):
            if s_list[min_value] > s_list[j]:
                min_value = j

        if s_list[scan_s] > s_list[min_value]:
            temp = s_list[scan_s]
            s_list[scan_s] = s_list[min_value]
            s_list[min_value] = temp
    s_str = ''.join(s_list)
    return s_str

def is_anagram_sort_t(t_list):

    for scan_t in range(len(t_list) - 1):
        min_value = scan_t
        for j in range(scan_t + 1, len(t_list)):
            if t_list[min_value] > t_list[j]:
                min_value = j

        if t_list[scan_t] > t_list[min_value]:
            temp = t_list[scan_t]
            t_list[scan_t] = t_list[min_value]
            t_list[min_value] = temp
    t_str = ''.join(t_list)
    return t_str

# print(is_anagram("listen", "silent"))


def remove_vowels(s: str):
    """
    Write an algorithm to remove all vowels from a string without replace() built-in method.
    You can write iteratively or recursively.

    e.g.
    remove_vowels("hello") -> "hll"
    remove_vowels("world") -> "wrld"
    remove_vowels("what") -> "wht"
    remove_vowels("") -> ""
    remove_vowels("a") -> ""

    :param s: string
    :return: string removed vowels
    """
    # pass
    s_list = list(s)
    result = []
    vowels = "aiueoAIUEO"
    for i in range(len(s_list)):
        if s_list[i] not in vowels:
            result.append(s_list[i])
    s_str = ''.join(result)
    return s_str

# print(remove_vowels("hello"))