# -*- coding=utf-8 -*-

"""TP1: test."""

# Comprehension created list of tuple
comp_list = [(i, j) for i in range(3)
             for j in range(i + 1, i + 4)]
print(f'This is my first list. It has been created by list comprehension.')
print(comp_list)
print()

# The result dictionnary
d_res = {}
print(f'The result dictionnary based on the above list')
for i, j in comp_list:
    if i not in d_res:
        d_res[i] = [j]
    else:
      #      print(j)
        d_res[i].append(j)
print(f'd_res')
print(d_res)

my_dictionary = {
    key: (ind1)
    for (key, ind1) in comp_list
}
print(f'my_dic')
print(my_dictionary)
