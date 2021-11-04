"""Utilities for manipulating lists."""


def head(input_list):
    months = input_list[0]
    return months

head(['Jan', 'Feb', 'Mar'])
    
"""Return the first item of the input list.

    months = input_list[0]

    For example:

      >>> head(['Jan', 'Feb', 'Mar'])
      'Jan'
"""



def tail(input_list):
    
    months = input_list[1:]
    return months

tail(['Jan', 'Feb', 'Mar'])
    
"""Return a new list of all items, excluding the first item.



    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar']

"""


def last(input_list):

    months = input_list[-1]
    return [months]
last(['Jan', 'Feb', 'Mar'])

"""Return the last item of the input list.

    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'

"""




def top(input_list):

    months = input_list[:-1]
    return months
top(['Jan', 'Feb', 'Mar'])

"""Return all elements of the input list except the last.

    For example:

    >>> top(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']

"""



def first_three(input_list):
    months = input_list[:3]
    return months

first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])



"""Return the first three elements of the input list.
    

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

"""



def last_five(input_list):
    nums = input_list[-5:]
    return nums

last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

"""Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

"""



def middle(input_list):
    nums = input_list[2:8]
    return nums
middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27]



)


"""Return all elements of input_list except the first two and the last two.

    For example:

    >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15, 18, 21]

"""



def inner_four(input_list):
    nums = input_list[2:6]
    return nums

inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
"""Return the third, fourth, fifth, and sixth elements of input_list.

    For example:

    >>> inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15]

"""



def inner_four_end(input_list):
    nums = input_list[-6:-2]
    return nums
inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])



"""Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

    This function should return those elements in a list, in the exact order
    described above.

    For example:

    >>> inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [12, 15, 18, 21]

"""



def replace_head(input_list):
    
    multiples = input_list[0] = 42 
    pass

replace_head([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

"""Replace the head of input_list with the value 42 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples == [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    True

"""



def replace_third_and_last(input_list):
    input_list[3] = 37 
    input_list[-1] = 37
    pass

replace_third_and_last([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
"""Replace third and last elements of input_list with 37 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_third_and_last(multiples)
    >>> multiples == [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]
    True

"""



def replace_middle(input_list):
    input_list[2:8] = [42, 37]

    pass
replace_middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

"""Replace all elements of a list but the first two and last two with 42 and 37.

    After the replacement, 42 and 37 should appear in that order in input_list.

    Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples == [0, 3, 42, 37, 24, 27]
    True

"""



def delete_third_and_seventh(input_list):
    del input_list[2]
    del input_list[6]
    pass
delete_third_and_seventh(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])

"""Remove third and seventh elements of input_list and return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_third_and_seventh(notes)
    >>> notes == ['Do', 'Re', 'Fa', 'So', 'La', 'Do']
    True

"""



def delete_middle(input_list):
    del input_list[2:6]
    pass
delete_middle(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])

"""Remove all elements from input_list except the first two and last two.

    Return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_middle(notes)
    >>> notes == ['Do', 'Re', 'Ti', 'Do']
    True

"""


# This is the part were we actually run the doctests.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")
