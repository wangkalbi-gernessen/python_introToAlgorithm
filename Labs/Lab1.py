"""
Basic python string problems -- no loops.
"""


def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
    """
    return "Hello " + name + "!"


def make_tags(tag, word):
    """
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
    In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
    """
    return "<" + tag + ">" + word + "</" + tag + ">"



def first_two(string):
    """
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
    If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string ""
    yields the empty string "".
    """

    # list_item = list(string)
    # if len(list_item) >= 2:
    #     boy = list_item[0:2]
    #     return ''.join(boy)
    # elif len(list_item) < 2:
    #     return ''.join(list_item)

    if len(string) >= 2:
        return string[0:1]
    elif len(string) < 2:
        return string

def first_half(string):
    """
    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
    """

    # item_list = list(string)
    # len_items = len(item_list)
    # half_len_items = len_items // 2
    # item_list[half_len_items:len_items] = []
    # return ''.join(item_list)

    half_string = len(string) // 2
    answer = string[:half_string]
    return answer

def without_end(string):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".
    The string length will be at least 2.
    """
    fullname = list(string)
    fullname.pop(len(fullname) - 1)
    fullname.pop(0)
    return ''.join(fullname)

def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of each.
    The strings will be at least length 1.
    """
    a_val = list(a)
    b_val = list(b)
    a_val.pop(0)
    b_val.pop(0)
    a_string = ''.join(a_val)
    b_string = ''.join(b_val)
    return a_string + b_string


def left2(string):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
    The string length will be at least 2.
    """
    fullname = list(string)
    first_two_val = fullname[0:2]
    fullname[0:2] = []
    fullname += first_two_val
    return ''.join(fullname)