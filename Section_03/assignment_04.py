# Assignment 4:

"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.

Example:

    For example, the below function call should return ['mike', 'john']

    last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])

"""

# Your code below:
def last_list(*args):
    return args[-1]

print(last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john']))


def test(**kwargs):
    return kwargs

print(test(action='nke', prix=123))
































# Solution:

# def last_list(*args):
#     return args[-1 :len(args)]
