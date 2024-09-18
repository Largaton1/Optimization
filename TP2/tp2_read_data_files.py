# -*- coding=utf-8 -*-

"""TP2: Module for extract admissible cells data from file."""

from argparse import ArgumentParser
from pathlib import Path
from sys import exit as sys_exit


# ============================================================================ #
#                                   CONSTANTS                                  #
# ============================================================================ #
ADM_BLOCK = 'ADMISSIBLE'
ROW_LIM_BLOCK = 'ROW_LIMIT'
COL_LIM_BLOCK = 'COLUMN_LIMIT'
END_BLOCK = '}'


# ============================================================================ #
#                                   FUNCTIONS                                  #
# ============================================================================ #
# ---------------------------------------------------------------------------- #
#                                  Extraction                                  #
# ---------------------------------------------------------------------------- #
def extract_adm_cells(file_path):
    """Return a NetworkX graph containing admissible cells data."""
    l_adm_cells = []

    with open(file_path, 'r') as f_in:
        # Extract data from header
        header = f_in.readline()
        n_row, n_col = (int(str_num) for str_num in header.split())
        n_diag = n_row + n_col -1
        # Initialize row/column limits lists
        l_row_limit = [0] * n_row
        l_col_limit = [0] * n_col
        l_diag_limit = [0] * n_diag
        # Extract data from blocks
        block_name = ''
        for line in f_in:
            line_split = line.split()
            if not block_name:
                block_name = line_split[0]
            elif line_split[0] == END_BLOCK:
                # End of block
                block_name = ''
            elif block_name == ADM_BLOCK:
                add_adm_cell(l_adm_cells, line_split)
            elif block_name == ROW_LIM_BLOCK:
                add_row_limit(l_row_limit, line_split, n_row)
            elif block_name == COL_LIM_BLOCK:
                # Add column limit
                add_column_limit(l_col_limit, line_split, n_col)
            else:
                sys_exit(f'ERROR: line = {line}')

    return l_adm_cells, l_row_limit, l_col_limit,l_diag_limit,


def add_adm_cell(l_adm_cells, line_split):
    """Add the admissible cell coordinates.

    Parameters
    ----------
    l_adm_cells : list of couple of int
        List of admissible cells
    line_split : list of str
        File line separated by space
    """
    row_i, col_j = int(line_split[0]), int(line_split[1])
    l_adm_cells.append((row_i, col_j))


def add_row_limit(l_row_limit, line_split, n_row):
    """Add row limit.

    Parameters
    ----------
    l_row_limit : list of int
        List of row limits
    line_split : list of str
        File line separated by space
    n_row : int
        Number of rows
    """
    row_i = int(line_split[0])
    row_i_lim = int(line_split[1])
    try:
        l_row_limit[row_i] = row_i_lim
    except IndexError:
        sys_exit(f'ERROR: {row_i} >= number row in header {n_row}')


def add_column_limit(l_col_limit, line_split, n_col):
    """Add column limit.

    Parameters
    ----------
    l_col_limit : list of int
        List of column limits
    line_split : list of str
        File line separated by space
    n_col : int
        Number of columns
    """
    col_j = int(line_split[0])
    col_j_lim = int(line_split[1])
    try:
        l_col_limit[col_j] = col_j_lim
    except IndexError:
        sys_exit(f'ERROR: {col_j} >= number row in header {n_col}')
        
def add_diag_limit(l_diag_limits, line_split, n_diag):
    """Add diagonal limit.

    Parameters
    ----------
    l_diag_limits : list of int
        List of diagonal limits
    line_split : list of str
        File line separated by space
    n_diag : int
        Number of diagonal
    """
    diag_d = int(line_split[0])
    diag_d_lim = int(line_split[1])
    try:
        l_diag_limits[diag_d] = diag_d_lim
    except IndexError:
        sys_exit(f'ERROR: {diag_d} >= number row in header {n_diag}')        


# ---------------------------------------------------------------------------- #
#                                Argument Parser                               #
# ---------------------------------------------------------------------------- #
def get_adm_cells_data():
    """Give admissible cells data.

    Yields
    ------
    list of tuple
        Admissible cells
    list of int
        Row limits
    list of int
        Column limits
    """
    argparser = ArgumentParser()
    argparser.add_argument(
        '--all-data', dest='all_data', action='store_true',
        help='Compute all the data',
    )
    arg = argparser.parse_args()

    if arg.all_data:
        for k in range(5):
            file = Path(f'data/admissible_cells_{k}.data')
            print()
            print(f'== FILE: {file.name} ==')
            print()
            yield extract_adm_cells(file)
    else:
        file = Path('data/admissible_cells.data')
        print()
        print(f'== FILE: {file.name} ==')
        print()
        yield extract_adm_cells(file)


# ============================================================================ #
#                                     MAIN                                     #
# ============================================================================ #
if __name__ == '__main__':
    FILE_PATH = 'data/admissible_cells.data'
    adm_cells, row_limit, col_limit,diag_limit, = extract_adm_cells(FILE_PATH)

    # Print to verify
    m = len(row_limit)
    n = len(col_limit)
    d = len(diag_limit)

    # Draw matr
    array = [['F' for _ in range(n)] for _ in range(m)]

    for (i, j) in adm_cells:
        array[i][j] = 'T'

    print('-' * 40)
    print()
    print('\t'.join(str(lim) for lim in col_limit))
    print()
    for i, row in enumerate(array):
        print('\t'.join(row), f'\t{row_limit[i]}')
    print()
