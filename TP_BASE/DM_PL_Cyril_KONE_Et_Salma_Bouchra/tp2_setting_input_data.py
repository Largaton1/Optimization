# -*- coding=utf-8 -*-

# Do not take these comments into consideration
# pylint: disable=too-many-arguments

"""TP2 - input data """


# ============================================================================ #
def get_adm_cells_data_bis():
#the list of admissible cases
    l_adm_cells=[
        (0,  0),
        (0,  1),
        (1,  0),
        (1,  2),
        (1,  3),
        (2,  1),
        (2,  4),
        (3,  2),
        (3,  4)
    ]
#the list of row limits
    l_row_limits=[9,10,15,2]
#the list of columns limits
    l_col_limits=[7,5,9,4,8]


    l_diag_limits = [7,2,0,8,4,2,8,0]

    return  l_adm_cells, l_row_limits, l_col_limits,l_diag_limits,