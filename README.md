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
