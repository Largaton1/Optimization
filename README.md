# TP2 – How data structures affect models
An illustration with the admissible cells problem
Given a grid rectangular grid Tm×n of boxes called cells. Some of these cells are admis
le, the others are non-admissible. Also are given m + n non-negative integers l0 . . . lm−1,
. . cn−1. The goal is to fill in the admissible cells with positive integers such as:
— The sum of the numbers allocated on the admissible cells on row i should be less or
equal than li;
— The sum of the numbers allocated on the admissible cells on column j should be less
or equal than cj;
— The total sum of all these numbers should be maximum.

Example: Let:
(m = 4) l0 = 9 l1 = 10 l2 = 15 l3 = 2
(n = 5) c0 = 7 c1 = 5 c2 = 9 c3 = 4 c4 = 8
and the set of admissible cells is:
A = {(0, 0), (0, 1), (1, 0), (1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 4)}
where the first index corresponds to the row, second index to the column number.

# Easy example then more complex ones
## Data files reader API
In TP2 folder you can find tp2 read data files.py. There are functions to extract admissible cells from files in data directory, and a function to parse command line’s argument.
It is not necessary to understand how they work, just how to use them.
Especially, the function get adm cells data lets you to iterate over it to get admissible
cells data from each file. You can use it as following:
for adm_cells, row_limits, col_limits in get_adm_cells_data():
# adm_cells: list of tuple (row_i, col_j)
# corresponding to admissible cells
# row_limits: list of row limits (int)
# col_limits: list of column limits (int)
solve_admissible_cells(adm_cells, row_limits, col_limits)
In fact, get adm cells data yield the three lists instead of returning them. It allows
to iterate over the function in a stream way.
## Let play!
Question 1.
Use the pre-structured Python3 program in TP BASE/TP0/base model.py and
write the admissible cells model.
Question 2.
Run your program with:
(.venv_3) python3 your_prog.py
What is the solution?
In order to test more complex instances, you can run your program like this:
(.venv_3) python3 your_prog.py --all-data > tp2_all_results.log
Question 3.
Run the program for all the data and plot the CPU time according number of
number of variables, and according the number of constraints, with the method of
your choice.
Tip: you can use CTRL+F on tp2 all results.log and search for FILE word in
order to find very quickly statistics.

