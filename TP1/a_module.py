# -*- coding=utf-8 -*-

"""Module for test."""


# ============================================================================ #
#                               DECLARE A FUNCTION                             #
# ============================================================================ #
def print_objects(*args):
    """The function documentation.

    Print all the objects (0 or +) given in argument.
    Note that the function does not have a return statement.
    You can just write 'return' at the end but it is useless.
    """
    # enumerate() returns additionaly a counter with the objects in args
    for k, obj in enumerate(args):
        print(f'- Object num. {k + 1}:')
        print(f'\t{obj}')
        print()


def return_the_last_element_list(my_list):
    """Return the last element of a list.

    Don't implement this function at home please!
    """
    return my_list[-1]
