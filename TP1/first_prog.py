# -*- coding=utf-8 -*-

"""You should add this docstring.

You can follow coding conventions as PEP8.
"""

from a_module import print_objects  # Loaded module named 'a_module.py'


# ============================================================================ #
#                        COMMON PYTHON BUILT-IN OBJECTS                        #
# ============================================================================ #
# ---------------------------------------------------------------------------- #
#                                    Trivial                                   #
# ---------------------------------------------------------------------------- #
an_integer: int = 1  # immutable
a_float: float = 0.5  # immutable
a_boolean: bool = True  # idem
a_char: str = 'c'  # idem
a_string: str = 'string'  # idem

# Note: in python you are not obliged to indicate the types of variables.
#   You can do it to help you understand objects' structures

# Constant convention:
#   upper-case, at the opposite of lower-case for variables
A_CONSTANT = 'i_am_a_string_constant'

# ---------------------------------------------------------------------------- #
#                                  None Object                                 #
# ---------------------------------------------------------------------------- #
NONE_OBJECT = None  # near-equivalent of null

assert NONE_OBJECT is None  # use 'is' only to compare object with None

# ---------------------------------------------------------------------------- #
#                                     Tuple                                    #
# ---------------------------------------------------------------------------- #
# Main properties:
# - immutable
# - ordered (with indices)

# Constructor
empty_tuple = ()
initialized_tuple = (1, 2, 3)
heterogeneous_tuple = (1, 'a_string', True)  # int, str, bool type

# Iteration on values O(n)
for value in initialized_tuple:
    print(f'values from initialized_tuple')
    print(value)

# Iteration both on index's value and values with enumerate() built-in function
for index, value in enumerate(initialized_tuple):
    assert initialized_tuple[index] == value

# - containing test O(n)
assert 1 in initialized_tuple

# ---------------------------------------------------------------------------- #
#                                     List                                     #
# ---------------------------------------------------------------------------- #
# - same as tuple but mutable i.e. we can change the value at an index
empty_list = []
initialized_list = [0, 4, 2]

# Acces to an element knowing the index
assert initialized_list[1] == 4

# Change the value at index 1
initialized_list[1] = 5
assert initialized_list[1] == 5

# ---------------------------------------------------------------------------- #
#                                  Dictionary                                  #
# ---------------------------------------------------------------------------- #
# Properties:
# - mutable
# - unordered: key associated to an object
# - iteration on keys O(n)
# - test key in dictionary O(1)

# Constructor
empty_dictionary = {}
initialized_dict = {
    'key1': 3,
    5: 'value_at_key_5',
}

# Accessing an element
assert initialized_dict[5] == 'value_at_key_5'

# Iterate on both keys and associated values
#   - use .items() object method
for key, value in initialized_dict.items():
    assert value == initialized_dict[key]

# ---------------------------------------------------------------------------- #
#                                      Set                                     #
# ---------------------------------------------------------------------------- #
# - mutable
# - unordered
# - iteration on values O(n)
# - test value in set O(1)
empty_set = set()
initialized_set = {0, 4, 5}  # '{ }' same as dict but with no asociated ': val'

assert 2 not in initialized_set

# ---------------------------------------------------------------------------- #
# List and dictionary comprehension
# - to create a filled list / dictionary directly with constructor
# ---------------------------------------------------------------------------- #

# ~*~ LIST ~*~
#
# - inline
my_list = [(i, j) for i in range(5) for j in range(5, 10)]
# - several lines: for beauty
my_list = [
    (i, j)
    for i in range(5)
    for j in range(5, 10)
]
# = [(0, 5), (0, 6), ..., (1, 5), ..., (4, 9)]
# -> Note: take care of loop indices and their order

# ~*~ DICTIONARY ~*~
#
#   - inline
dictionary = {key: value for (key, value) in my_list}
#   - several lines
dictionary = {
    key: value
    for (key, value) in my_list
}
# = {0: 9, 1: 9, ..., 4: 9}
# -> TODO: explain it


# ============================================================================ #
#                                   CONDITIONS                                 #
# ============================================================================ #

print('BOOLEAN TEST')
print('------------')
if a_boolean:
    print('The boolean is equal to True')

print()
print('IF ELIF ELSE CONDITIONS')
print('-----------------------')
# You can compare this with a switch case
if my_list:
    print('my_list is not empty')
elif dictionary:
    print('my_list is empty but not dictionary')
else:
    print('my_list and dictionary are empty')


# ============================================================================ #
#                     CALL A FUNCTION OF A LOADED MODULE                       #
# ============================================================================ #

print()
print('USE OF MODULE FUNCTION')
print('----------------------')
# The function arguments are just the variable identifiers,
#   no pointer or anything else!
print_objects(my_list, dictionary)  # function imported from a_module.py file


# ============================================================================ #
#                                  USING LOOPS                                 #
# ============================================================================ #

print()
print('FOR ON DICT KEYS')
print('-----------')
for key in dictionary:
    # dictionary[key] returns the value associated with the key 'key'
    print(f'KEY = {key} -> VALUE = {dictionary[key]}')  # f-string for format
    # in f-string, you can format string with variables inplace (use '{var}')

print()
print('WHILE LOOP')
print('----------')
k = 0
while k < len(my_list):  # len(my_list) give the list length
    print(f'my_list[{k}] = {my_list[k]}')
    k += 1

print()
print('FOR ON DICT KEYS AND VALUES')
print('---------------------------')
# Loop on both keys and values in the dictionary
for (key, value) in dictionary.items():
    print(f'KEY = {key} -> VALUE = {value}')
# Exactly the same, but cleaner
print(f'Exactly the same, but cleaner')
for key, value in dictionary.items():
    print(f'KEY = {key} -> VALUE = {value}')
